from etl_pipeline.extract import extract_data
from etl_pipeline.transform import transform_data
from etl_pipeline.load import load_data

file_path = "E:/DataEngineer/etl-movies/data/top1000.csv"

def run_pipeline():
    df = extract_data(file_path)
    clean_df = transform_data(df)
    load_data(clean_df, "top1000")

if __name__ == "__main__":
    run_pipeline()













