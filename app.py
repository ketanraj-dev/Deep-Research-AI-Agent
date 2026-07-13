import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager
from styles import CSS, JS, EXAMPLES, HEADER_HTML

load_dotenv(override=True)

_STEPS = [
    ("Planning",  "Planning searches"),
    ("Searching", "Searching the web"),
    ("Writing",   "Writing report"),
    ("Emailing",  "Sending email"),
]


def _status_html(done: int, finished: bool = False) -> str:
    """Build the progress-stepper HTML shown above the report."""
    items = []
    for i, (short, full) in enumerate(_STEPS):
        if i < done:
            cls, icon = "dr-step-done", "✓"
        elif i == done and not finished:
            cls, icon = "dr-step-active", "◉"
        else:
            cls, icon = "dr-step-pending", "○"
        items.append(
            f'<div class="dr-step {cls}">'
            f'<span class="dr-step-icon">{icon}</span>'
            f'<span class="dr-step-label">{full}</span>'
            f'</div>'
        )
        if i < len(_STEPS) - 1:
            items.append('<div class="dr-step-connector"></div>')

    outer_cls = "dr-status-done" if finished else "dr-status-running"
    return f'<div class="dr-status {outer_cls}">{"".join(items)}</div>'


async def run(query: str):
    if not query.strip():
        yield "", ""
        return

    done = 0
    yield _status_html(done), ""

    async for update in ResearchManager().run(query):
        if update.lstrip().startswith("#"):
            yield _status_html(len(_STEPS), finished=True), update
        else:
            if "Searches planned" in update:
                done = 1
            elif "Search complete" in update:
                done = 2
            elif "Report written" in update:
                done = 3
            elif "Email Sent" in update:
                done = 4
            yield _status_html(done), ""


def clear_all():
    return "", "", ""


with gr.Blocks(title="Deep Research", css=CSS) as ui:
    gr.HTML(HEADER_HTML)

    with gr.Row(elem_classes="dr-query-row"):
        query_textbox = gr.Textbox(
            placeholder="What do you want to investigate?",
            show_label=False,
            container=False,
            autofocus=True,
            elem_id="dr-query",
            scale=5,
        )
        run_button = gr.Button("Investigate", variant="primary", elem_id="dr-run", scale=1)
        clear_button = gr.Button("Clear", variant="secondary", elem_id="dr-clear", scale=0)

    gr.HTML('<div class="dr-examples-label">Try one</div>')
    gr.Examples(examples=EXAMPLES, inputs=query_textbox, elem_id="dr-examples")

    status_box = gr.HTML(elem_id="dr-status-box")
    report = gr.Markdown(elem_id="dr-report")

    run_button.click(run, inputs=query_textbox, outputs=[status_box, report])
    query_textbox.submit(run, inputs=query_textbox, outputs=[status_box, report])
    clear_button.click(clear_all, outputs=[query_textbox, status_box, report])


if __name__ == "__main__":
    ui.launch(js=JS, theme=gr.themes.Base())
