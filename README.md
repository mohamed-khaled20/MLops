# MLops - UI

* UI.py is the main file
* I built UI using [streamlit](https://streamlit.io/) and deployed it on [streamlit cloud](https://streamlit.io/cloud).
* Continous deployment is supported by [streamlit cloud](https://streamlit.io/cloud)
* Continous integration is used by providing [test_UI_CI.yaml](./github/workflows/test_UI_CI.yaml) file for Github actions, every time file is pushed for this repo, this file will automate the CI process by running the test in [test_UI.py](test/test_UI.py)
* You can access the streamlit application [here](https://mohamed-khaled20-mlops-ui-ui-8nv4zf.streamlitapp.com/)
