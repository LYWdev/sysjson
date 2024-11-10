import json
import re

# 오류가 있는 파일 목록
error_files = [
    "getusage.json",
    "getpriority.json",
    "inotify_init1.json",
    "getrandom.json",
    "madvise.json",
    "pkey_alloc.json"
]

def correct_json_syntax(filepath):
    """
    주어진 JSON 파일의 구문 오류를 자동으로 수정합니다.
    불필요한 콜론을 제거하고, 올바른 JSON 형식으로 재구성합니다.
    """
    with open(filepath, 'r') as file:
        content = file.read()
    
    # 불필요한 ': [' 또는 ': {' 패턴 제거
    content = re.sub(r'":\s*:', '":', content)
    
    try:
        # 수정된 내용을 JSON으로 파싱하여 유효성 확인
        data = json.loads(content)
        # 수정된 내용을 다시 저장
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Corrected JSON saved for {filepath}")
    except json.JSONDecodeError as e:
        print(f"Failed to correct {filepath}: {e}")
        print("Please manually verify the file.")

# 오류가 있는 파일 목록을 순회하며 수정 수행
for filename in error_files:
    correct_json_syntax(filename)

