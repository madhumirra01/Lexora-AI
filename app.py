
import streamlit as st
import html
from summarizer import summarize

st.set_page_config(
    page_title="Lexora AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- STYLING ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #f7f8fc;
    color: #20243a;
    font-family: 'DM Sans', sans-serif;
    font-size: 17px;
}

.block-container {
    max-width: 1450px;
    padding: 1.8rem 3rem 3rem;
}

header[data-testid="stHeader"] {
    background: #f7f8fc;
}

#MainMenu, footer {
    visibility: hidden;
}

h1, h2, h3, h4 {
    font-family: 'Manrope', sans-serif !important;
    color: #20243a !important;
}

p {
    color: #667085;
}

/* HEADER */
.brand {
    font-family: 'Manrope', sans-serif;
    font-size: 27px;
    font-weight: 800;
    color: #20243a;
    letter-spacing: -0.8px;
}

.brand span {
    color: #6956d9;
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px 0 20px;
    border-bottom: 1px solid #e8eaf2;
    margin-bottom: 34px;
}

.top-tag {
    font-size: 14px;
    font-weight: 600;
    color: #697189;
    background: #ffffff;
    border: 1px solid #e5e7ef;
    padding: 9px 14px;
    border-radius: 30px;
}

/* HERO */
.hero-title {
    font-family: 'Manrope', sans-serif;
    font-size: clamp(42px, 4.5vw, 58px);
    line-height: 1.25;
    font-weight: 800;
    letter-spacing: -1.8px;
    color: #20243a;
    margin-bottom: 12px;
}

.gradient-text {
    color: #6956d9;
}

.hero-subtitle {
    color: #697189;
    font-size: 18px;
    line-height: 1.9;
    max-width: 760px;
}

.hero-badge {
    color: #6956d9;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.7px;
    margin-bottom: 15px;
}

/* PANELS */
.panel-title {
    font-family: 'Manrope', sans-serif;
    color: #20243a;
    font-size: 23px;
    font-weight: 800;
    letter-spacing: -0.4px;
}

.panel-subtitle {
    color: #798196;
    font-size: 16px;
    line-height: 1.8;
    margin-top: 7px;
    margin-bottom: 22px;
}

.section-label {
    color: #858da1;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 10px;
}

/* SOURCE TEXT */
div[data-testid="stTextArea"] textarea {
    background: #ffffff !important;
    color: #252a40 !important;
    border: 1px solid #dfe3ed !important;
    border-radius: 12px !important;
    padding: 18px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 17px !important;
    line-height: 1.9 !important;
}

div[data-testid="stTextArea"] textarea:focus {
    border-color: #9a8be8 !important;
    box-shadow: 0 0 0 2px rgba(105,86,217,0.09) !important;
}

div[data-testid="stTextArea"] label {
    font-size: 16px !important;
}

/* SLIDER */
div[data-testid="stSlider"] {
    background: #ffffff;
    border: 1px solid #e6e9f2;
    border-radius: 12px;
    padding: 15px 18px 7px;
}

div[data-testid="stSlider"] label {
    font-size: 16px !important;
}

div[data-testid="stSlider"] [data-testid="stMarkdownContainer"] {
    font-size: 16px !important;
}

/* BUTTONS */
div.stButton > button {
    width: 100%;
    min-height: 56px;
    background: #6956d9;
    color: #ffffff;
    border: 1px solid #6956d9;
    border-radius: 10px;
    font-family: 'DM Sans', sans-serif;
    font-size: 17px;
    font-weight: 700;
    transition: 0.2s ease;
}

div.stButton > button:hover {
    background: #5845c5;
    color: #ffffff;
    border-color: #5845c5;
    box-shadow: 0 5px 14px rgba(105,86,217,0.16);
}

div[data-testid="stDownloadButton"] button {
    width: 100%;
    min-height: 50px;
    background: #f2efff;
    color: #5946c3;
    border: 1px solid #e1dbff;
    border-radius: 10px;
    font-size: 16px;
    font-weight: 700;
}

div[data-testid="stDownloadButton"] button:hover {
    background: #eae5ff;
    color: #4936b4;
}

/* RESULT */
.result-box {
    background: #ffffff;
    border: 1px solid #e6e9f2;
    border-left: 4px solid #7968e3;
    border-radius: 12px;
    padding: 25px;
    color: #343a50;
    font-size: 17px;
    line-height: 2;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
}

.result-label {
    color: #6956d9;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 14px;
}

/* STATISTICS */
div[data-testid="stMetric"] {
    background: #ffffff;
    border: 1px solid #e5e8f0;
    border-radius: 12px;
    padding: 17px;
}

div[data-testid="stMetricLabel"] {
    color: #7b8498 !important;
    font-size: 14px !important;
}

div[data-testid="stMetricValue"] {
    color: #252a40 !important;
    font-size: 27px !important;
}

/* FEATURE DETAILS */
.mini-feature {
    color: #697189;
    font-size: 15px;
    line-height: 1.9;
    padding: 16px 0;
    border-bottom: 1px solid #eceef4;
}

.mini-feature b {
    color: #30364d;
    font-size: 16px;
}

.info-chip {
    display: inline-block;
    background: #f0edff;
    border: 1px solid #e5dfff;
    border-radius: 8px;
    padding: 10px 13px;
    color: #5946c3;
    font-size: 14px;
    font-weight: 600;
}

hr {
    border-color: #e9ecf3 !important;
}

.footer {
    text-align: center;
    color: #8991a4;
    font-size: 14px;
    padding: 28px 0 5px;
}

/* RESPONSIVE */
@media (max-width: 800px) {
    .block-container {
        padding: 1rem 1rem 2rem;
    }

    .hero-title {
        font-size: 39px;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 16px;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown("""
<div class="topbar">
    <div class="brand">✨ Lexora <span>AI</span></div>
    <div class="top-tag">TEXT SUMMARIZATION · TEXTRANK</div>
</div>
""", unsafe_allow_html=True)


# ---------- INTRO ----------
st.markdown("""
<div class="hero-badge">READ SMARTER, NOT LONGER</div>

<div class="hero-title">
    Less text. <span class="gradient-text">More insight.</span>
</div>

<div class="hero-subtitle">
    Turn lengthy articles and documents into concise summaries.
    Extract the important information and spend less time reading.
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")


# ---------- LANDSCAPE WORKSPACE ----------
left, right = st.columns([0.9, 1.1], gap="large")

with left:
    st.markdown("""
    <div class="panel-title">✦ Summary workspace</div>
    <div class="panel-subtitle">
        Customize the output and generate a summary of your text.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-label">SUMMARY LENGTH</div>',
        unsafe_allow_html=True
    )

    sentence_count = st.slider(
        "Number of sentences",
        min_value=1,
        max_value=8,
        value=3,
        label_visibility="collapsed"
    )

    st.write("")

    st.markdown("""
    <div class="info-chip">✦ TextRank algorithm</div>

    <div class="mini-feature">
        <b>Extractive summarization</b><br>
        Selects important sentences from your original text.
    </div>

    <div class="mini-feature">
        <b>Lightweight processing</b><br>
        No large Transformer model downloads required.
    </div>

    <div class="mini-feature">
        <b>Summary statistics</b><br>
        Review word counts and text reduction after processing.
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    generate = st.button("✨  Generate Summary", type="primary")


with right:
    st.markdown("""
    <div class="panel-title">Your source text</div>
    <div class="panel-subtitle">
        Paste an article, research paper, report, or any lengthy text below.
    </div>
    """, unsafe_allow_html=True)

    article_text = st.text_area(
        "Source text",
        placeholder=(
            "Start typing or paste your text here...\n\n"
            "For best results, use text containing several complete sentences."
        ),
        height=390,
        label_visibility="collapsed"
    )

    st.caption(f"✍️  {len(article_text.split()):,} words")


# ---------- RESULTS ----------
if generate:
    if not article_text.strip():
        st.warning("Please paste some text into the source text panel first.")

    else:
        try:
            with st.spinner("Analyzing sentences and ranking key information..."):
                summary, elapsed = summarize(
                    article_text,
                    sentence_count=sentence_count
                )

            original_words = len(article_text.split())
            summary_words = len(summary.split())

            compression = (
                (1 - summary_words / original_words) * 100
                if original_words else 0
            )

            st.write("")
            st.divider()

            st.markdown(
                '<div class="section-label">GENERATED OUTPUT</div>',
                unsafe_allow_html=True
            )

            st.markdown("### Your summary")

            st.markdown(f"""
            <div class="result-box">
                <div class="result-label">✦ SUMMARY</div>
                {html.escape(summary)}
            </div>
            """, unsafe_allow_html=True)

            st.write("")
            st.markdown("#### Summary insights")

            col1, col2, col3 = st.columns(3)

            col1.metric("Original words", f"{original_words:,}")
            col2.metric("Summary words", f"{summary_words:,}")
            col3.metric("Text reduction", f"{compression:.1f}%")

            st.caption(f"Processing time: {elapsed:.3f} seconds")

            st.write("")

            st.download_button(
                "📥  Download Summary",
                data=summary,
                file_name="lexora_summary.txt",
                mime="text/plain"
            )

        except Exception as error:
            st.error(f"Unable to generate summary: {error}")


# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    ✨ Lexora AI · Less text. More insight.
</div>
""", unsafe_allow_html=True)
