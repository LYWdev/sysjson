import os
import json

def analyze_structure(data, level=0):
    """
    재귀적으로 JSON 데이터의 자료 구조를 분석하고 상하관계 및 타입을 출력합니다.
    """
    indent = "  " * level  # 계층 수준에 따라 들여쓰기 설정
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{indent}- {key}: {type(value).__name__}")
            analyze_structure(value, level + 1)
    elif isinstance(data, list):
        print(f"{indent}- List of {len(data)} items")
        if data:
            analyze_structure(data[0], level + 1)  # 리스트의 첫 번째 항목으로 타입 분석
    else:
        print(f"{indent}- Value: {type(data).__name__}")

def analyze_json_files_in_directory(directory="."):
    """
    디렉토리 내 모든 JSON 파일의 구조를 분석합니다.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as file:
                    data = json.load(file)
                    print(f"\nAnalyzing {filename}:\n{'=' * (len('Analyzing ' + filename) + 1)}")
                    analyze_structure(data)
            except json.JSONDecodeError as e:
                print(f"Failed to parse {filename}: {e}")
            except Exception as e:
                print(f"Error analyzing {filename}: {e}")

# 실행
analyze_json_files_in_directory(".")

