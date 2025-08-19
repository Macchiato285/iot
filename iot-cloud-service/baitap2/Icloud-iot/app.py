from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# --- 1. Kết nối Firebase ---
cred = credentials.Certificate("icloud-iot-services-firebase-adminsdk-fbsvc-5a655dbcbd.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# --- 2. Khởi tạo Flask ---
app = Flask(__name__)

# --- 3. Route nhập dữ liệu ---
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        station_id = request.form.get("station_id", "").strip()
        name = request.form.get("name", "").strip()
        time_str = request.form.get("time", "").strip()

        try:
            time_dt = datetime.fromisoformat(time_str)
        except Exception:
            time_dt = datetime.utcnow()

        def to_float(val):
            try:
                return float(val)
            except (TypeError, ValueError):
                return None

        temperature = to_float(request.form.get("temperature"))
        humidity = to_float(request.form.get("humidity"))
        wind = to_float(request.form.get("wind"))
        pressure = to_float(request.form.get("pressure"))

        data = {
            "id": station_id,
            "name": name,
            "time": time_dt,
            "temperature": temperature,
            "humidity": humidity,
            "wind": wind,
            "pressure": pressure
        }

        # Lưu mỗi bản ghi là một document mới
        db.collection("environment_data").add(data)

        return redirect(url_for("view_data"))

    return render_template("index.html")


# --- 4. Route xem dữ liệu + lọc theo ngày ---
@app.route("/view", methods=["GET", "POST"])
def view_data():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    query = db.collection("environment_data")

    if start_date and end_date:
        try:
            start_dt = datetime.fromisoformat(start_date)
            end_dt = datetime.fromisoformat(end_date)
            query = query.where("time", ">=", start_dt).where("time", "<=", end_dt)
        except Exception:
            pass  # nếu parse lỗi thì bỏ lọc

    query = query.order_by("time", direction=firestore.Query.DESCENDING)
    docs = query.stream()

    data_list = []
    for doc in docs:
        record = doc.to_dict()
        if isinstance(record.get("time"), datetime):
            record["time_str"] = record["time"].strftime("%Y-%m-%d %H:%M")
        else:
            record["time_str"] = str(record.get("time"))
        data_list.append(record)

    return render_template("list.html", data_list=data_list, start_date=start_date, end_date=end_date)


if __name__ == "__main__":
    app.run(debug=True)
