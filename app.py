import streamlit as st
import google.generativeai as genai
from datetime import datetime, timedelta

# ページ設定
st.set_page_config(page_title="AI見積エージェント", layout="wide")
st.title("🎯 キャンペーン戦略・見積AIエージェント")

# APIキー設定（最新のPwZ0キー）
genai.configure(api_key="AIzaSyAFsilIzfMzV2oBZWeanWEIkTYlH7ePwZ0")

# 入力エリア
st.markdown("### 📋 キャンペーン情報を貼り付けてください")
minutes = st.text_area("スプレッドシートから情報を貼り付けてください", height=200, placeholder="（例）当選者数 10,000名、期間 3ヶ月...")

if st.button("🚀 見積・分析を開始する"):
    if not minutes.strip():
        st.warning("⚠️ 内容が空欄です！情報を入力してください。")
    else:
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        with st.spinner("貴社専用ロジックで計算中..."):
            tab1, tab2, tab3 = st.tabs(["📊 詳細見積書", "👥 ターゲット分析", "📝 ヒアリング事項"])
            
            # 見積ロジックの設定
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
            ・抽選費用: 5
