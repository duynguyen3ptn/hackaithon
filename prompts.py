# System prompt for meeting analysis
SYSTEM_INSTRUCTION = """
You are a professional AI assistant specializing in meeting analysis.

Your input is a transcript of a meeting, and your task is to:
1. Summarize the key points of the meeting.
2. Extract actionable items as bullet points, including:
   - Task description
   - Responsible person (if mentioned)
   - Deadline or time frame (if mentioned)

Format your output as follows:

📝 Summary:
- [Concise summary of the meeting discussion]

✅ Action Items:
- [Task 1] — [Responsible person] — [Deadline if mentioned]
- [Task 2] — …

Transcript:
\"\"\"
[Paste the transcript here]
\"\"\"
"""

# Meeting transcripts
SCRIPT1 = """ 
Chào mọi người, hôm nay chúng ta họp để cập nhật tiến độ dự án "Hệ thống quản lý khách hàng"...
// ...existing script1 content...
"""

SCRIPT2 = """ 
    Chào cả team, mình bắt đầu họp sprint review nhé. Tuần này mình muốn nghe cập nhật từ mọi người và lên kế hoạch cho sprint mới.

    Mình đã hoàn thành xong phần backend cho chức năng reset mật khẩu. Hiện tại API đã test ổn trên staging. Lâm có thể giúp mình viết unit test cho flow này không?

    Ok, Lâm sẽ hỗ trợ. Bên frontend sao rồi?

    Giao diện trang "Quản lý nhóm người dùng" đã hoàn thành khoảng 80%. Mình đang chờ Nam cập nhật lại danh sách role từ backend để binding chính xác.

    Nam đã push chưa?

    Mình đã push rồi, nhưng còn thiếu phần lọc theo loại tài khoản. Mình sẽ bổ sung trước 3 giờ chiều nay.

    Rồi. Mình thấy tuần này CI/CD bị lỗi deploy production đúng không?

    Đúng rồi. Do thiếu `ENV_SECRET` khi chạy GitHub Actions. Mình đã thêm vào secrets config rồi. Bây giờ flow chạy ổn định lại rồi.

    Tốt. Về sprint mới, nhóm mình cần hoàn thiện phần phân quyền chi tiết cho từng loại tài khoản. Hoa sẽ phụ trách UI. Tuấn xử lý phần logic phân quyền trong API. Nam kiểm tra và cập nhật lại tài liệu Postman.

    Ok, Hoa cần gì thì ping Lâm, Lâm đã xử lý phần tương tự ở module "Nhóm người dùng" rồi.

    Cảm ơn anh. Vậy Tuấn confirm giúp em luồng phân quyền có giống flow hiện tại không nha?

    Ừ, chiều mình họp riêng 30 phút để chốt flow cũng được.

    Mình sẽ tạo task trên Jira hết chiều nay nhé. Mọi người nhớ update status trước 9h sáng hàng ngày.

    Rõ rồi.

    Dạ ok.

    Tất cả ổn. Cảm ơn anh.
"""
