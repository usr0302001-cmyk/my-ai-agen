import streamlit as st
import google.generativeai as genai
from datetime import datetime, timedelta

# 画面のタイトルと設定
st.set_page_config(page_title="AI見積エージェント", layout="wide")
st.title("🎯 キャンペーン戦略・見積AIエージェント")

# あなたのGemini APIキーを設定（後で安全な方法に変えられますが、まずは直書きでOK）
genai.configure(api_key="AIzaSyDW-1zglX-8H3X9Zt2dVYXX76L0dSoG46c")

# 入力欄
minutes = st.text_area("💼 議事録またはキャンペーン案をペーストしてください", height=200)

if st.button("🚀 分析・見積を開始する"):
    if minutes:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        with st.spinner("AIが戦略を立案中..."):
            # あのサイトのようにタブで表示を分ける
            tab1, tab2, tab3 = st.tabs(["📊 見積・条件案", "👥 ターゲット・ペルソナ", "📝 ヒアリングシート"])
            
            with tab1:
                deadline = (datetime.now() + timedelta(days=3)).strftime("%Y/%m/%d")
                res = model.generate_content(f"議事録から施策名、マストバイ条件、概算見積を詳細に出して。確認期限は{deadline}として。:\n{minutes}")
                st.markdown(res.text)
                
            with tab2:
                res = model.generate_content(f"この施策の想定ターゲットと詳細なペルソナ像を3名分作成して。:\n{minutes}")
                st.markdown(res.text)
                
            with tab3:
                res = model.generate_content(f"クライアントに確認すべき課題と、戦略的なヒアリング項目を5つ提案して。:\n{minutes}")
                st.markdown(res.text)
    else:
        st.warning("議事録を入力してください。")
