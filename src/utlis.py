import base64
from IPython.display import Image, display, Markdown

def query_response(chain):
    question = input("Enter your question: ")
    response = chain.invoke(question)

    # Styling using HTML in Markdown
    styled_output = f"""
    <div style="font-family: Arial, sans-serif; line-height: 1.6; margin-top: 20px;">
        <p style="color: #2c3e50; font-size: 18px; font-weight: bold;">
            Question:
        </p>
        <p style="background-color: #ecf0f1; color: #34495e; padding: 10px; border-radius: 5px;">
            {question}
        </p>
        <p style="color: #2c3e50; font-size: 18px; font-weight: bold;">
            Response:
        </p>
        <p style="background-color: #dff9fb; color: #1e272e; padding: 10px; border-radius: 5px;">
            {response}
        </p>
    </div>
    """

    # Display styled output
    display(Markdown(styled_output))


def display_base64_image(base64_code):
    image_data = base64.b64decode(base64_code)
    display(Image(data=image_data))