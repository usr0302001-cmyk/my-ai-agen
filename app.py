import streamlit as st

st.set_page_config(page_title="Fanspot見積システム", layout="wide")
st.title("🎯 Fanspot 案件見積エージェント")

# サイドバーに入力項目
st.sidebar.header("📋 条件入力")
period = st.sidebar.number_input("施策期間 (月数)", min_value=1, value=2)
winners = st.sidebar.number_input("当選者数", min_value=0, value=10000, step=1000)
is_iw = st.sidebar.radio("インスタントウィン", ["有り", "無し"])
update = st.sidebar.number_input("ページ更新回数", min_value=0, value=1)
has_ocr = st.sidebar.radio("OCR解析機能", ["有り", "無し"])

if st.sidebar.button("🚀 見積もりを算出"):
    # 事務局と目検のロジック計算
    j_months = period + 1
    m_count = winners * 2
    m_cost = m_count * 1000
    
    # 各種費用の計算
    init = 3500000 + 1000000 + (3000000 if has_ocr=="有り" else 0) + (3000000 if is_iw=="有り" else 0) + m_cost + 50000
    oper = (650000 * period) + (400000 * j_months) + (1000000 * update)
    total = init + oper

    # 画面表示
    st.header(f"合計費用（税抜）: {total:,}円")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**■ 初期費用: {init:,}円**")
        st.write(f"・設定/実装: 4,500,000円\n・OCR: {'3,000,000' if has_ocr=='有り' else '0'}円\n・IW: {'3,000,000' if is_iw=='有り' else '0'}円\n・目検 ({m_count:,}枚): {m_cost:,}円")
    with col2:
        st.markdown(f"**■ 運用費用: {oper:,}円**")
        st.write(f"・月額費用: {650000*period:,}円\n・事務局 ({j_months}ヶ月): {400000*j_months:,}円\n・更新 ({update}回): {1000000*update:,}円")
    
    st.divider()
    st.warning("⚠️ 注釈：LINE配信費用および制作費用は含まれておりません。")
else:
    st.info("左側のメニューで条件を選び、ボタンを押してください。")
