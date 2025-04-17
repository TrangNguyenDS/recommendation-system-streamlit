import streamlit as st

# Trang phân cụm khách hàng
def data_insight(products_clean, rating_clean):
    st.image("images/insight.jpeg", width=1000)
    st.title("Một số thông tin về dữ liệu")

    st.markdown("### 🛍️ Dữ liệu sản phẩm")
    st.dataframe(products_clean.head(10))
    st.markdown("### ⭐ Dữ liệu đánh giá sản phẩm")
    st.dataframe(rating_clean.head(10))

    
    # Tính các chỉ số
    num_products = products_clean['product_id'].nunique()
    num_users = rating_clean['user_id'].nunique()
    num_ratings = rating_clean.shape[0]
    
    # Merge để lấy thông tin price, product_name
    eda_merged = rating_clean.merge(products_clean[['product_id', 'price', 'product_name']], on='product_id', how='left')

    # User đánh giá nhiều nhất
    top_reviewer = rating_clean['user_id'].value_counts().idxmax()
    top_reviewer_count = rating_clean['user_id'].value_counts().max()

    # User chi tiêu nhiều nhất
    user_spend = eda_merged.groupby('user_id')['price'].sum()
    top_spender = user_spend.idxmax()
    top_spend_amount = user_spend.max()

    # User rating 5 sao nhiều nhất
    one_star_users = rating_clean[rating_clean['rating'] == 5]['user_id'].value_counts()
    top_one_star_user = one_star_users.idxmax()
    top_one_star_count = one_star_users.max()

    # Sản phẩm bán chạy nhất (nhiều đánh giá nhất)
    top_product_id = rating_clean['product_id'].value_counts().idxmax()
    top_product_name = products_clean.loc[products_clean['product_id'] == top_product_id, 'product_name'].values[0]

    # Sản phẩm bán ít nhất (ít đánh giá nhất)
    least_product_id = rating_clean['product_id'].value_counts().idxmin()
    least_product_name = products_clean.loc[products_clean['product_id'] == least_product_id, 'product_name'].values[0]

    col1, col2, col3 = st.columns(3)

    # ---------- CỘT 1: THỐNG KÊ CHUNG ----------
    with col1:
        st.markdown("### 📊 Thống kê tổng quan")
        st.markdown(f"🛍️ **Số sản phẩm:**<br><span style='font-size:16px'>{num_products}</span>", unsafe_allow_html=True)
        st.markdown(f"👤 **Số người dùng:**<br><span style='font-size:16px'>{num_users}</span>", unsafe_allow_html=True)
        st.markdown(f"⭐ **Số lượt đánh giá:**<br><span style='font-size:16px'>{num_ratings}</span>", unsafe_allow_html=True)

    # ---------- CỘT 2: USER ----------
    with col2:
        st.markdown("### 🙋‍♂️ Người dùng nổi bật")
        st.markdown(f"✍️ **Review nhiều nhất:**<br><span style='font-size:15px'>{top_reviewer} ({top_reviewer_count} lần)</span>", unsafe_allow_html=True)
        st.markdown(f"💰 **Chi tiêu nhiều nhất:**<br><span style='font-size:15px'>{top_spender} ({top_spend_amount:,.0f} VNĐ)</span>", unsafe_allow_html=True)
        st.markdown(f"😍 **Rating 5⭐ nhiều nhất:**<br><span style='font-size:15px'>{top_one_star_user} ({top_one_star_count} lần)</span>", unsafe_allow_html=True)

    # ---------- CỘT 3: SẢN PHẨM ----------
    with col3:
        st.markdown("### 📦 Sản phẩm nổi bật")
        st.markdown(f"🔥 **Nhiều đánh giá nhất:**<br><span style='font-size:15px'>{top_product_name[:30]}...</span>", unsafe_allow_html=True)
        st.markdown(f"🥶 **Ít đánh giá nhất:**<br><span style='font-size:15px'>{least_product_name[:30]}...</span>", unsafe_allow_html=True)


    st.subheader("📦 Top 10 Nhóm Hàng Phổ Biến Nhất")
    st.image("images/top10_nhomhang.png", width=1000)

    st.subheader("🛍️ Top 20 Tên Sản Phẩm Phổ Biến Nhất")
    st.image("images/top20_ten_sp_pho_bien.png", width=1000)
    
    st.subheader("🎻 Phân bố giá theo nhóm sản phẩm")
    st.image("images/phanbogia.png", width=1000)
    
    st.subheader("📦 Phân bố Rating theo Nhóm Sản Phẩm")
    st.image("images/phanborating.png", width=1000)
    
    st.subheader("📈 Tương Quan giữa Giá và Rating theo Nhóm Sản Phẩm")
    st.image("images/tuongquan_gia_nhom_sp.png", width=1000)

    st.subheader("💰 Giá Trung Bình Theo Nhóm Sản Phẩm")
    st.image("images/gia_trung_binh_nhom.png", width=1000)

    st.subheader("⭐ Rating Trung Bình Theo Nhóm Sản Phẩm")
    st.image("images/rating_trung_binh_nhom.png", width=1000)

    st.subheader("⭐ Biểu đồ rating theo phần trăm")
    st.image("images/rating_percent.png", width=1000)

    st.subheader("⭐ Top Sản Phẩm Nhận Được Nhiều Đánh Giá 5 Sao")
    st.image("images/top_sp_5_star.png", width=1000)

    st.subheader("⭐ Top Nhóm Sản Phẩm Nhận Được Nhiều Đánh Giá 5 Sao")
    st.image("images/top_nhom_sp_5_star.png", width=1000)

    st.subheader("⚠️ Top Sản Phẩm Nhận Được Nhiều Đánh Giá 1 Sao")
    st.image("images/top_sp_1_star.png", width=1000)

    st.subheader("📊 Phân bố độ dài mô tả sản phẩm")
    st.image("images/phan_bo_do_dai_mo_ta.png", width=1000)

    st.markdown("### ☁️ Wordcloud mô tả sản phẩm")
    st.image("images/wordcloud.png", width=1000)