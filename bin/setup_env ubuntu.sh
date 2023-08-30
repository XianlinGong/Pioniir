python -m venv venv
activate() {
    . venv/bin/activate
    echo "install requirements to virtual environment"
    pip install -r requirements.txt
}

activate