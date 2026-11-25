import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Công cụ tính lãi đơn và lãi kép",
    page_icon="💰",
    layout="centered"
)

# Tiêu đề
st.title("💰 CÔNG CỤ TÍNH LÃI ĐƠN VÀ LÃI KÉP")
st.write("Ứng dụng tính toán số tiền khách hàng nhận được theo hai phương pháp.")

st.divider()

# Nhập dữ liệu
st.subheader("📌 Nhập thông tin")

C = st.number_input(
    "Số vốn ban đầu (đồng)",
    min_value=0,
    value=100_000_000,
    step=10_000_000
)

i = st.number_input(
    "Lãi suất mỗi kỳ (%)",
    min_value=0.0,
    value=1.0,
    step=0.1
)

n = st.number_input(
    "Số kỳ tính lãi",
    min_value=1,
    value=3,
    step=1
)

# Chuyển lãi suất từ phần trăm sang số thập phân
rate = i / 100

# Nút tính toán
if st.button("🧮 TÍNH TOÁN", type="primary"):

    # Công thức lãi đơn
    An = C * (1 + rate * n)

    # Công thức lãi kép
    Bn = C * ((1 + rate) ** n)

    # Tính tiền lãi
    lai_don = An - C
    lai_kep = Bn - C

    st.divider()
    st.subheader("📊 KẾT QUẢ TÍNH TOÁN")

    col1, col2 = st.columns(2)

    with col1:
        st.success("LÃI ĐƠN")
        st.metric(
            label="Tổng số tiền nhận được",
            value=f"{An:,.0f} đồng"
        )
        st.write(f"Tiền lãi: {lai_don:,.0f} đồng")

    with col2:
        st.info("LÃI KÉP")
        st.metric(
            label="Tổng số tiền nhận được",
            value=f"{Bn:,.0f} đồng"
        )
        st.write(f"Tiền lãi: {lai_kep:,.0f} đồng")

    st.divider()

    # So sánh kết quả
    st.subheader("📈 So sánh")

    chenhlech = Bn - An

    st.write(
        f"Số tiền lãi kép cao hơn lãi đơn: "
        f"**{chenhlech:,.0f} đồng**"
    )

    # Biểu đồ
    st.bar_chart({
        "Số tiền nhận được": {
            "Lãi đơn": An,
            "Lãi kép": Bn
        }
    })

st.caption("Ứng dụng tính toán lãi đơn và lãi kép bằng Python & Streamlit.")
