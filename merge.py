import json
import glob

def combine_json_files(output_file):
    combined_data = []

    for file_name in glob.glob("*.json"):
        try:
            with open(file_name, 'r') as f:
                data = json.load(f)
                combined_data.append(data)
        except json.JSONDecodeError as e:
            # 에러 발생 시 파일명, 행, 열 정보와 함께 파일 내용을 출력
            print(f"\nError decoding JSON in file {file_name}: {e.msg} at line {e.lineno} column {e.colno}")
            with open(file_name, 'r') as f:
                file_content = f.read()
            print(f"Content of {file_name}:\n{file_content}\n")
            continue

    # 결과를 solution.json 파일에 저장
    with open(output_file, 'w') as f:
        json.dump(combined_data, f, indent=2)
    print(f"Combined data written to {output_file}")

combine_json_files("solution.json")

