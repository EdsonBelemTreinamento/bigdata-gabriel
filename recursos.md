
python -m venv myenv 

cd myenv
cd Scripts

pip install sqlalchemy
pip install sqlalchemy.orm
pip install pandas
pip install psycopg2-binary
pip install fastapi
pip install uvicorn
pip install pydantic
pip install streamlit
pip install plotly


python -m uvicorn main:app --reload