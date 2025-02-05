import gradio as gr
from exa_py import Exa

# ✅ Initialize Exa client
EXA_API_KEY = "2453df71-05e0-4784-88e4-d3ea891aec43"
exa_client = Exa(EXA_API_KEY)

def researcher(topic):
    """Search Exa for the latest research on a topic and return highlights."""
    response = exa_client.search_and_contents(
        query=f"Latest research on {topic}",
        use_autoprompt=True,
        num_results=5,
        highlights=True
    )

    if not response.results:
        return "❌ No relevant research found."

    # Format results
    research_summary = "### 📖 Research Summary\n\n"
    for result in response.results:
        highlights = result.highlights or ["No summary available."]
        research_summary += f"📄 [{result.title}]({result.url})\n📝 {highlights[0]}\n\n"

    return research_summary

# ✅ Create Gradio Interface
iface = gr.Interface(
    fn=researcher,
    inputs=gr.Textbox(label="Enter Research Topic"),
    outputs=gr.Markdown(),
    title="🔍 Athena Research",
    description="Enter a topic to get high-quality research summaries from the web."
)

# ✅ Launch the app
iface.launch()
