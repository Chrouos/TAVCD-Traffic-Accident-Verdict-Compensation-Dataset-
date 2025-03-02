---

# TAVCD (Traffic Accident Verdict Compensation Dataset)

[English Version](https://github.com/Chrouos/TAVCD-Traffic-Accident-Verdict-Compensation-Dataset-/blob/main/README_en.md)

## **簡介**
TAVCD (Traffic Accident Verdict Compensation Dataset) 是針對 **台灣交通事故判決書** 進行標註的數據集，涵蓋法院判決內容、事故資訊、人員傷害、財產損失與賠償金額等詳細資訊。本數據集適用於 **學術研究、法律分析、機器學習模型訓練**，並可用於 NLP 任務，如文本分類、命名實體識別 (NER) 和資訊擷取。

### **數據概覽**
- **數據規模**：共 **1000** 筆裁判書
- **標註方式**：由兩位標記者 (`Labeler_1` & `Labeler_2`) 獨立標記，確保準確性
- **數據格式**：JSONL (`.jsonl`)

---

## **目錄結構與數據內容**

### **1. 判決書原始數據**
> 存放於 `Source/Verdict/` 目錄，包含原始判決內容與處理後的文本。

- **`judgement`**：完整判決書文本（含換行符號）
- **`cleanJudgement`**：去除特殊符號的純文字版本
- **`opinion`**：法官的判決內容（擷取自 `judgement`）
- **`cleanOpinion`**：法官判決內容的純文字版本（去除特殊符號）

### **2. 標註數據**
> 位於 `Source/Labeler_1/` 和 `Source/Labeler_2/` 目錄，存放人工標註結果。

- **`name`**：標註的欄位名稱（如「事故日期」、「賠償金額總額」等）
- **`value`**：標註內容
- **`the_surrounding_words`**：標註內容的上下文資訊
- **`position`**：標註內容在判決書中的位置
  - `start_position` & `end_position`（對應文本內的字元索引）

### **3. 機器學習訓練數據**
> 提供 NLP 模型訓練用數據，格式適用於資訊擷取與生成式 AI 應用。

- **`finetuning_training_data_golden.jsonl`**：
  - `input`：完整判決書內容
  - `output`：包含所有標註欄位的 JSON 結構
- **`finetuning_training_data.jsonl`**：
  - `subject`：標註的欄位名稱
  - `input`：標註內容的前後文（基於標點符號切分）
  - `output`：擷取的內容

---

## **程式碼**

+ `regular_fields.py` - 定義標註欄位類別，例如 **事故資訊、傷勢、賠償金額** 等，以及哪些欄位需要採用，需要用欄位填入`template_fields`。
+ `processed_to_format.py` - 轉換數據集格式，適用於不同應用場景。

---

## **標記欄位**
TAVCD 數據集涵蓋以下類別資訊：

### **(1) 事故資訊**
- 事故日期
- 事發經過
- 事故車出廠日期

### **(2) 人員傷害與賠償**
- 傷勢
- 職業
- 居家看護天數 / 費用 / 每日金額
- 住院看護天數 / 費用 / 每日金額
- 醫療費用
- 精神賠償
- 每日工作收入
- 工作損失天數 / 損失金額

### **(3) 車輛與財產損失**
- 折舊方法
- 耐用年數
- 修車費用（塗裝 / 工資 / 烤漆 / 鈑金 / 零件 / 材料）
- 財產損失
- 交通費用

### **(4) 判決賠償與保險給付**
- 被告肇責比例
- 賠償金額總額
- 保險給付金額

### **(5) 營業損失**
- 每日營業收入
- 營業損失天數 / 損失金額

### **(6) 其他資訊**
- 其他（特殊情況、未分類損失）
- 備註

---

## **使用方式**
TAVCD 數據集可用於：
1. **法律分析**：研究台灣法院對交通事故賠償的判決趨勢。
2. **機器學習 / NLP 訓練**：用於判決書解析、資訊擷取與分類。
3. **文本標註應用**：關鍵資訊標註、關係抽取、事件識別。

### **簡單閱讀數據**
```python
import json

def load_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

# 加載數據
data = load_jsonl("finetuning_training_data_golden.jsonl")

# 顯示第一筆數據
print(json.dumps(data[0], indent=2, ensure_ascii=False))
```

### **轉換數據格式**
```bash
python ./processed_to_format.py \
    --type format_data_text \
    --data_path finetuning_training_data_golden.jsonl \
    --output_path ./instruction/
```

---

## **貢獻與聯絡**
如果您對本數據集有建議或發現錯誤，請透過以下方式聯繫我們：
- 提交 [GitHub Issue](https://github.com/Chrouos/TAVCD-Traffic-Accident-Verdict-Compensation-Dataset-/issues)
- 直接聯絡數據集管理員

---

## **授權**
本數據集僅供 **學術研究與非商業用途**，使用時請遵守相關法規與隱私政策。