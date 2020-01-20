from app import create_app

app = create_app("development")

@app.shell_context_processor
def make_shell_processor():
    return dict(
        app = app
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0")
