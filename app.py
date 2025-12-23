import streamlit as st
import google.generativeai as genai
from datetime import datetime, timedelta

# ページ設定
st.set_page_config(page_title="AI見積エージェント", layout="wide")
st.title("🎯 キャンペーン戦略・見積AIエージェント")

# APIキー設定
genai.configure(api_key="AIzaSyAFsilIzfMzV2oBZWeanWEIkTYlH7ePwZ0")

# 入力エリア
st.markdown("### 📋 キャンペーン情報を貼り付けてください")
minutes = st.text_area("スプレッドシートから当選者数や期間などの情報を貼り付けてください", height=200)

if st.button("🚀 見積・分析を開始する"):
    if not minutes.strip():
        st.warning("⚠️ 内容が空欄です！スプレッドシートから情報をコピーして貼り付けてください。")
    else:
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        with st.spinner("貴社専用ロジックで計算中..."):
            tab1, tab2, tab3 = st.tabs(["📊 詳細見積書", "👥 ターゲット分析", "📝 ヒアリング事項"])
            
            # ご提示いただいた「見積ロジック」をここに集約
            logic = """
            あなたは熟練のキャンペーンプランナーとして、以下の【貴社専用単価ルール】を厳守して見積を作成してください。
            
            【システム費】
            ・Fanspot 初期設定費用: 3,500,000円
            ・Fanspot レシート応募実装費: 1,000,000円
            ・FanSpot インスタントウィン機能実装費: 3,000,000円
            ・FanSpot ページ更新費: 1,000,000円/回
            ・Fanspot 月額費用/運用管理: 650,000円/月
            ・Fanspot レシートOCR即時解析: 3,000,000円
            
            【事務局費】
            ・問合せ事務局対応費: 400,000円
            ・目検作業費: 1枚につき1,000円
              ※計算式: (想定応募数) × 1,000円。応募数は当選数の2倍として計算すること。
            ・抽選費用: 50,000円/回
            
            【出力形式】
            各項目の小計と、すべての合計金額（税込・税抜）を明示してください。
            """
            
            try:
                with tab1:
                    res1 = model.generate_content(f"{logic}\n\n以下の情報を元に算出してください：\n{minutes}")
                    st.markdown(res1.text)
                with tab2:
                    res2 = model.generate_content(f"詳細なターゲットペルソナを3名作成して：\n{minutes}")
                    st.markdown(res2.text)
                with tab3:
                    res3 = model.generate_content(f"クライアントへの戦略的ヒアリング項目を5つ提案して：\n{minutes}")
                    st.markdown(res3.text)
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
