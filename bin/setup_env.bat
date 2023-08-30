python -m venv venv
activate() {
    call .\venv\Scripts\activate
    echo "install requirements to virtual environment"
    pip install -r requirements.txt
}

activate