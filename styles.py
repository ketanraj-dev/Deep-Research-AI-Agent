EXAMPLES = [
    "Most popular AI Agent frameworks in 2026",
    "Most commercially successful Agentic AI implementations in 2026",
    "Celebrities who don't like cheese",
]

HEADER_HTML = """
<div class="dr-brand">
    <div class="dr-brand-left">
        <div class="dr-mark">
            <span class="dr-bar dr-bar-1"></span>
            <span class="dr-bar dr-bar-2"></span>
            <span class="dr-bar dr-bar-3"></span>
        </div>
        <div class="dr-titles">
            <h1>Deep<span class="dr-sep">/</span>Research</h1>
            <p>Multi-agent web investigation &mdash; powered by OpenAI &amp; Gemini</p>
        </div>
    </div>
    <button id="dr-theme-btn" onclick="drToggleTheme()" title="Toggle dark / light mode">◐ Theme</button>
</div>
"""

CSS = """
/* ── Reset helpers ── */
*, *::before, *::after { box-sizing: border-box; }

/* ── Design tokens ── */
.gradio-container {
    --dr-bg:          #fafaf7;
    --dr-surface:     #ffffff;
    --dr-surface-alt: #f3f3ef;
    --dr-line:        #0c0c0d;
    --dr-line-soft:   #deded7;
    --dr-text:        #0c0c0d;
    --dr-muted:       #6f6f72;
    --dr-amber:       #ecad0a;
    --dr-blue:        #209dd7;
    --dr-purple:      #753991;
    --dr-green:       #2a9d5c;

    max-width: 1080px !important;
    margin: 0 auto !important;
    padding: 2.5rem 2rem 5rem !important;
    background: var(--dr-bg) !important;
    color: var(--dr-text) !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial,
                 sans-serif !important;
    transition: background 0.25s, color 0.25s !important;
}

/* Dark theme overrides (toggled via body.dr-dark) */
body.dr-dark .gradio-container,
.gradio-container.dark,
.dark .gradio-container {
    --dr-bg:          #0b0b0c;
    --dr-surface:     #161618;
    --dr-surface-alt: #1e1e22;
    --dr-line:        #f0f0eb;
    --dr-line-soft:   #2a2a2e;
    --dr-text:        #f0f0eb;
    --dr-muted:       #8a8a8e;
}

body { background: var(--dr-bg, #fafaf7); transition: background 0.25s; }

/* ── Header ── */
.dr-brand {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 1.25rem;
    border-bottom: 3px solid var(--dr-line);
    margin-bottom: 2.5rem;
}

.dr-brand-left {
    display: flex;
    align-items: center;
    gap: 1.4rem;
}

.dr-mark {
    display: flex;
    flex-direction: column;
    gap: 5px;
    width: 38px;
    flex-shrink: 0;
}

.dr-bar   { height: 7px; display: block; border-radius: 1px; }
.dr-bar-1 { background: var(--dr-amber);  width: 100%; }
.dr-bar-2 { background: var(--dr-blue);   width: 70%;  }
.dr-bar-3 { background: var(--dr-purple); width: 45%;  }

.dr-titles h1 {
    font-size: clamp(1.8rem, 4vw, 2.6rem);
    font-weight: 900;
    letter-spacing: -0.045em;
    margin: 0;
    line-height: 0.95;
    text-transform: uppercase;
    color: var(--dr-text);
}

.dr-sep {
    color: var(--dr-amber);
    font-weight: 300;
    margin: 0 0.04em;
}

.dr-titles p {
    font-family: ui-monospace, "SF Mono", Menlo, monospace;
    font-size: 0.68rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin: 0.5rem 0 0;
    color: var(--dr-muted);
}

/* Theme toggle */
#dr-theme-btn {
    background: transparent;
    border: 1.5px solid var(--dr-line-soft);
    color: var(--dr-muted);
    padding: 0.4rem 0.85rem;
    font-size: 0.75rem;
    cursor: pointer;
    border-radius: 2px;
    transition: border-color 0.15s, color 0.15s;
    font-family: ui-monospace, monospace;
    letter-spacing: 0.1em;
    white-space: nowrap;
    flex-shrink: 0;
}
#dr-theme-btn:hover { border-color: var(--dr-amber); color: var(--dr-amber); }

/* ── Query row ── */
.dr-query-row {
    gap: 0 !important;
    align-items: stretch !important;
}

#dr-query, #dr-query > div, #dr-query .wrap, #dr-query .form, #dr-query .block {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    border-radius: 0 !important;
}

#dr-query textarea, #dr-query input {
    background: var(--dr-surface) !important;
    color: var(--dr-text) !important;
    border: 2px solid var(--dr-line) !important;
    border-radius: 0 !important;
    padding: 1.05rem 1.2rem !important;
    font-size: 1.05rem !important;
    font-family: inherit !important;
    box-shadow: none !important;
    line-height: 1.45 !important;
    resize: none !important;
    min-height: 56px !important;
    transition: border-color 0.15s, box-shadow 0.15s !important;
}

#dr-query textarea:focus, #dr-query input:focus {
    outline: none !important;
    border-color: var(--dr-blue) !important;
    box-shadow: 5px 5px 0 0 var(--dr-blue) !important;
}

#dr-query textarea::placeholder, #dr-query input::placeholder {
    color: var(--dr-muted) !important;
    opacity: 1 !important;
}

#dr-run {
    background: var(--dr-amber) !important;
    color: #0c0c0d !important;
    border: 2px solid var(--dr-line) !important;
    border-left: none !important;
    border-radius: 0 !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.14em !important;
    font-size: 0.85rem !important;
    box-shadow: none !important;
    transition: background 0.15s, color 0.15s, transform 0.08s !important;
    min-width: 140px !important;
    padding: 1rem 1.4rem !important;
}
#dr-run:hover  { background: var(--dr-purple) !important; color: #fff !important; }
#dr-run:active { transform: translate(2px, 2px) !important; }

#dr-clear {
    background: var(--dr-surface-alt) !important;
    color: var(--dr-muted) !important;
    border: 2px solid var(--dr-line) !important;
    border-left: none !important;
    border-radius: 0 !important;
    font-size: 0.8rem !important;
    box-shadow: none !important;
    padding: 1rem 0.9rem !important;
    transition: color 0.15s, background 0.15s !important;
    min-width: 70px !important;
}
#dr-clear:hover { color: var(--dr-text) !important; background: var(--dr-surface) !important; }

/* ── Examples ── */
.dr-examples-label {
    font-family: ui-monospace, monospace;
    font-size: 0.62rem;
    letter-spacing: 0.28em;
    color: var(--dr-muted);
    text-transform: uppercase;
    margin: 2rem 0 0.85rem;
    display: flex;
    align-items: center;
    gap: 0.85rem;
}
.dr-examples-label::after {
    content: "";
    flex: 1;
    height: 1px;
    background: var(--dr-line-soft);
}

#dr-examples, #dr-examples > div, #dr-examples .wrap, #dr-examples .block {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    box-shadow: none !important;
}
#dr-examples label, #dr-examples .label-wrap, #dr-examples > div > .label-wrap {
    display: none !important;
}
#dr-examples table {
    border-collapse: separate !important;
    border-spacing: 0 !important;
    width: auto !important;
    background: transparent !important;
    border: none !important;
}
#dr-examples thead { display: none !important; }
#dr-examples tbody { background: transparent !important; }
#dr-examples tr {
    background: transparent !important;
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
    border: none !important;
}
#dr-examples td, #dr-examples button {
    background: var(--dr-surface) !important;
    border: 1.5px solid var(--dr-line-soft) !important;
    padding: 0.65rem 1rem !important;
    cursor: pointer !important;
    transition: border-color 0.15s, color 0.15s, transform 0.1s !important;
    font-size: 0.88rem !important;
    color: var(--dr-text) !important;
    border-radius: 0 !important;
    margin: 0 !important;
    text-align: left !important;
    box-shadow: none !important;
}
#dr-examples td:hover, #dr-examples button:hover {
    border-color: var(--dr-purple) !important;
    color: var(--dr-purple) !important;
    transform: translateY(-1px);
}

/* ── Progress stepper ── */
#dr-status-box { margin-top: 2rem; }

.dr-status {
    display: flex;
    align-items: center;
    gap: 0;
    padding: 1.1rem 1.4rem;
    background: var(--dr-surface);
    border: 1.5px solid var(--dr-line-soft);
    overflow-x: auto;
}

.dr-step {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    white-space: nowrap;
    font-size: 0.8rem;
    padding: 0.2rem 0;
}

.dr-step-icon {
    font-size: 1rem;
    line-height: 1;
}

.dr-step-label {
    font-family: ui-monospace, "SF Mono", Menlo, monospace;
    font-size: 0.72rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

.dr-step-pending .dr-step-icon,
.dr-step-pending .dr-step-label {
    color: var(--dr-muted);
    opacity: 0.55;
}

.dr-step-active .dr-step-icon {
    color: var(--dr-blue);
    animation: dr-pulse 1.4s ease-in-out infinite;
}
.dr-step-active .dr-step-label {
    color: var(--dr-blue);
    font-weight: 700;
}

.dr-step-done .dr-step-icon  { color: var(--dr-green); }
.dr-step-done .dr-step-label { color: var(--dr-text); }

.dr-status-done {
    border-color: var(--dr-green);
    border-width: 1.5px;
}
.dr-status-done .dr-step-active .dr-step-icon { animation: none; color: var(--dr-green); }

.dr-step-connector {
    flex: 1;
    min-width: 24px;
    height: 1px;
    background: var(--dr-line-soft);
    margin: 0 8px;
}

@keyframes dr-pulse {
    0%, 100% { opacity: 1;    transform: scale(1);    }
    50%       { opacity: 0.5; transform: scale(0.85); }
}

/* ── Report ── */
#dr-report {
    margin-top: 2rem !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--dr-text) !important;
}

#dr-report > div, #dr-report .prose { background: transparent !important; color: var(--dr-text) !important; }

#dr-report:not(:empty) {
    border-top: 1px solid var(--dr-line-soft) !important;
    padding-top: 2rem !important;
}

#dr-report h1 {
    font-size: 1.85rem;
    font-weight: 900;
    color: var(--dr-blue);
    border-bottom: 2px solid var(--dr-line);
    padding-bottom: 0.45rem;
    margin: 1.5rem 0 1rem;
    letter-spacing: -0.025em;
}
#dr-report h2 {
    font-size: 1.3rem;
    color: var(--dr-purple);
    font-weight: 800;
    margin-top: 1.75rem;
    letter-spacing: -0.015em;
}
#dr-report h3 {
    font-size: 1.08rem;
    color: var(--dr-text);
    font-weight: 800;
    margin-top: 1.5rem;
}
#dr-report p  { line-height: 1.72; margin: 0.75rem 0; }
#dr-report a  {
    color: var(--dr-blue);
    text-decoration: underline;
    text-decoration-thickness: 2px;
    text-underline-offset: 3px;
}
#dr-report a:hover { color: var(--dr-amber); }
#dr-report code {
    background: var(--dr-surface);
    border: 1px solid var(--dr-line-soft);
    padding: 0.1rem 0.4rem;
    font-size: 0.91em;
    border-radius: 2px;
}
#dr-report pre {
    background: var(--dr-surface);
    border: 1.5px solid var(--dr-line-soft);
    border-radius: 2px;
    padding: 1rem 1.25rem;
    overflow-x: auto;
}
#dr-report blockquote {
    border-left: 3px solid var(--dr-amber) !important;
    background: var(--dr-surface);
    padding: 0.85rem 1.25rem;
    margin: 1rem 0;
    color: var(--dr-text);
}
#dr-report ul, #dr-report ol { padding-left: 1.5rem; }
#dr-report li { margin: 0.35rem 0; line-height: 1.65; }
#dr-report table {
    border-collapse: collapse;
    border: 1.5px solid var(--dr-line);
    width: 100%;
    margin: 1rem 0;
}
#dr-report th, #dr-report td {
    border: 1px solid var(--dr-line-soft);
    padding: 0.5rem 0.85rem;
    text-align: left;
}
#dr-report th {
    background: var(--dr-surface);
    font-weight: 800;
    color: var(--dr-blue);
}

/* ── Copy button (injected by JS) ── */
#dr-copy-btn {
    display: block;
    margin: 1.5rem 0 0 auto;
    background: transparent;
    border: 1.5px solid var(--dr-line-soft);
    color: var(--dr-muted);
    padding: 0.45rem 1rem;
    font-size: 0.75rem;
    font-family: ui-monospace, monospace;
    letter-spacing: 0.1em;
    cursor: pointer;
    border-radius: 2px;
    transition: border-color 0.15s, color 0.15s;
}
#dr-copy-btn:hover { border-color: var(--dr-blue); color: var(--dr-blue); }
#dr-copy-btn.copied { border-color: var(--dr-green); color: var(--dr-green); }

/* ── Misc ── */
footer { display: none !important; }

/* ── Mobile ── */
@media (max-width: 700px) {
    .gradio-container { padding: 1.5rem 1rem 3rem !important; }
    .dr-brand { flex-wrap: wrap; gap: 0.75rem; }
    .dr-query-row { flex-direction: column !important; }
    #dr-run {
        border-left: 2px solid var(--dr-line) !important;
        border-top: none !important;
        width: 100% !important;
    }
    #dr-clear {
        border-left: 2px solid var(--dr-line) !important;
        border-top: none !important;
        width: 100% !important;
    }
    .dr-step-connector { min-width: 12px; }
}
"""

JS = """
() => {
    /* ── Auto-focus query box ── */
    const focusQuery = () => {
        const el = document.querySelector("#dr-query textarea, #dr-query input");
        if (el) { el.focus(); return true; }
        return false;
    };
    if (!focusQuery()) {
        let tries = 0;
        const iv = setInterval(() => { if (focusQuery() || ++tries > 20) clearInterval(iv); }, 100);
    }

    /* ── Dark / light theme toggle ── */
    window.drToggleTheme = function () {
        document.body.classList.toggle("dr-dark");
        const btn = document.getElementById("dr-theme-btn");
        if (btn) btn.textContent = document.body.classList.contains("dr-dark") ? "◑ Theme" : "◐ Theme";
    };

    /* ── Inject a Copy button after the report renders ── */
    const injectCopy = () => {
        const report = document.getElementById("dr-report");
        if (!report || !report.innerText.trim()) return;
        if (document.getElementById("dr-copy-btn")) return;
        const btn = document.createElement("button");
        btn.id = "dr-copy-btn";
        btn.textContent = "COPY REPORT";
        btn.onclick = () => {
            navigator.clipboard.writeText(report.innerText).then(() => {
                btn.textContent = "COPIED ✓";
                btn.classList.add("copied");
                setTimeout(() => { btn.textContent = "COPY REPORT"; btn.classList.remove("copied"); }, 2200);
            });
        };
        report.insertAdjacentElement("afterend", btn);
    };

    const obs = new MutationObserver(injectCopy);
    const startObs = () => {
        const report = document.getElementById("dr-report");
        if (report) { obs.observe(report, { childList: true, subtree: true, characterData: true }); }
        else { setTimeout(startObs, 200); }
    };
    startObs();
}
"""
