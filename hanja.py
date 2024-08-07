import csv

def load_hanja_dict_from_csv(filename):
    """
    CSV 파일에서 한자 데이터를 읽어 딕셔너리로 변환합니다.
    """
    hanja_dict = {}
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter='\t')
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                if len(row) >= 2:
                    hanja = row[0].strip()
                    meaning = row[1].strip()
                    hanja_dict[hanja] = meaning
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return hanja_dict

def process_input(hanja_dict):
    """
    사용자로부터 한자 텍스트를 입력받아 처리하고 결과를 TXT 파일로 저장합니다.
    """
    print("한자 텍스트를 입력하세요. 입력이 끝나면 'END'를 입력하세요.")
    input_text = []
    
    while True:
        line = input()
        if line.strip() == 'END':
            break
        input_text.append(line.strip())
    
    with open('hanja_matched.txt', 'w', encoding='utf-8') as f:
        for line in input_text:
            for char in line:
                if char in hanja_dict:
                    f.write(f"{char}\t{hanja_dict[char]}\n")
    
    print("처리 완료. 결과는 'hanja_matched.txt'에 저장되었습니다.")

if __name__ == "__main__":
    csv_filename = 'hanja_dict.csv'  # CSV 파일 경로
    hanja_dict = load_hanja_dict_from_csv(csv_filename)
    
    if hanja_dict:
        process_input(hanja_dict)
    else:
        print("한자 사전을 로드할 수 없습니다.")