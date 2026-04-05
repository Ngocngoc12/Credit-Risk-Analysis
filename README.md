# 📊 Dự án Phân tích Rủi ro Tín dụng (Credit Risk Analysis)

> **Context:** Đây là dự án thực tế thuộc vòng Technical Challenge cho vị trí Data Analyst Intern.

## 🎯 Mục tiêu dự án
Đánh giá sức khỏe danh mục tín dụng và phân tích tỷ lệ nợ xấu (Bad Rate) dựa trên dữ liệu nhân khẩu học, thu nhập và loại hình nhà ở của khách hàng. Từ đó, đưa ra các đề xuất hành động (Actionable Insights) để tối ưu hóa quy trình xét duyệt.

## 🛠️ Công cụ & Kỹ năng sử dụng
* **SQL:** Truy vấn, làm sạch và chuẩn bị dữ liệu (Data Preparation).
* **Python (Pandas, Seaborn):** Phân tích khám phá (EDA), đánh giá mức độ tương quan (Correlation Matrix) giữa các biến và rủi ro tín dụng.
* **Power BI:** Trực quan hóa dữ liệu, xây dựng Dashboard tương tác và kể chuyện dữ liệu (Data Storytelling).

## 💡 Key Insights (Phát hiện quan trọng)
1. **Tổng quan:** Tỷ lệ nợ xấu toàn hệ thống được kiểm soát ở mức an toàn là **1.69%**.
2. **Điểm nóng rủi ro (Red Flags):**
   * Nhóm nghề nghiệp **IT Staff** có tỷ lệ nợ xấu cao đột biến lên tới **5.00%**.
   * Khách hàng trẻ (20-30 tuổi) sống tại **Căn hộ văn phòng (Office apartment)** hoặc nhà thuê tiềm ẩn rủi ro vỡ nợ cao hơn các nhóm khác.
3. **Nhóm an toàn:** Khách hàng trên 40 tuổi thuộc nhóm *Core staff* hoặc *Managers* có tỷ lệ rủi ro rất thấp (< 1.5%).

## 📂 Cấu trúc dự án
* `1_sql_data_processing.py`: Script truy vấn và tiền xử lý dữ liệu từ Database.
* `2_python_eda.py`: Script phân tích chuyên sâu (EDA) bằng Python.
* `final_dataset_for_powerbi.csv`: Dữ liệu đã được làm sạch để đưa vào Dashboard.
* `application_record.csv` & `credit_record.csv`: Dữ liệu gốc (Raw data).

## 🚀 Đề xuất Giải pháp (Actionable Recommendations)
1. **Siết chặt phê duyệt:** Yêu cầu thêm điều kiện (VD: sao kê lương 6 tháng thay vì 3 tháng) đối với nhóm IT Staff và khách hàng dưới 30 tuổi ở nhà thuê/căn hộ văn phòng.
2. **Chuyển dịch tỷ trọng:** Đẩy mạnh các gói vay ưu đãi cho nhóm khách hàng trung niên và nhóm ngành quản lý/nhân sự để cân bằng lại rủi ro cho toàn bộ danh mục tín dụng.
