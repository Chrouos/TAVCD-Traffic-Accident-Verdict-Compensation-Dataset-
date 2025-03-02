這裡是你的 README 改進版本，強調清晰度、組織性與易讀性。我重新整理結構，使內容更直觀，並調整了一些措辭，以確保讀者能更快理解數據集的內容與用途。

---

# TAVCD (Traffic Accident Verdict Compensation Dataset)

[English Version](https://github.com/Chrouos/TAVCD-Traffic-Accident-Verdict-Compensation-Dataset-/blob/main/README_en.md)

## 簡介
TAVCD (Traffic Accident Verdict Compensation Dataset) 是一個針對 **台灣交通事故判決書** 進行標記的數據集，包含法院判決內容、事故資訊、人員傷害、財產損失與賠償金額等詳細資訊。本數據集適用於 **學術研究、法律分析、機器學習模型訓練**，並可作為 NLP 領域的標註數據。

### 數據規模
- **標註數據：** 共 **1000** 筆裁判書
- **標註方式：** 由兩位標記者 (`Labeler_1` & `Labeler_2`) 進行獨立標記，以確保數據的準確性
- **數據格式：** JSONL (`.jsonl`)

---

## 目錄結構與數據內容

### **1. 判決書原始數據**
位於 `Source/Verdict/` 目錄，包含原始判決內容與處理後的文本：
- **`judgement`**：完整判決書文本（含換行符號）
- **`cleanJudgement`**：去除特殊符號的純文字版本
- **`opinion`**：法官的判決內容（從 `judgement` 擷取）
- **`cleanOpinion`**：法官判決內容的純文字版本（去除特殊符號）

---

### **2. 標註數據**
標註數據位於 `Source/Labeler_1/` 和 `Source/Labeler_2/` 目錄：
- **`name`**：標註的欄位名稱（如「事故日期」、「賠償金額總額」等）
- **`value`**：標註的內容
- **`the_surrounding_words`**：標註內容的上下文資訊
- **`position`**：標註內容在判決書中的位置
  - `start_position` & `end_position`（對應文本內的字元索引）

---

### **3. 模型訓練數據**
用於機器學習與 NLP 訓練：
- **`finetuning_training_data_golden.jsonl`**：
  - `input`：完整判決書內容
  - `output`：包含所有標註欄位的 JSON 結構
- **`finetuning_training_data.jsonl`**：
  - `subject`：標註的欄位名稱
  - `input`：標註內容的前後文（基於標點符號切分）
  - `output`：擷取的內容

---

## 程式碼

+ `regular_fields.py`
  + 規則話欄位所屬，例如 `事發經過` 與 `傷勢` 等為字串欄位，`事故日期` 與 `事故車出廠日期` 是關於日期的欄位。
+ `labeler_to_processed.py`


## **標記欄位**
TAVCD 數據集涵蓋以下類別的資訊：

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
- 其他（其他損失或特殊資訊）
- 備註

---

## **使用方式**
TAVCD 數據集可用於：
1. **法律分析**：研究台灣法院對交通事故賠償的判決趨勢
2. **機器學習 / NLP 訓練**：訓練模型進行判決書解析與資訊擷取
3. **文本標註應用**：用於關鍵資訊標註、關係抽取、事件識別等研究

**處理方式（Python 範例）**
```python
import json

# 讀取 JSONL 格式數據
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

---

## **貢獻與聯絡**
如果您對本數據集有任何建議或發現錯誤，歡迎透過以下方式聯繫我們：
- 提交 [GitHub Issue](https://github.com/Chrouos/TAVCD-Traffic-Accident-Verdict-Compensation-Dataset-/issues)
- 直接聯絡數據集管理員

---

## **授權**
本數據集僅供 **學術研究與非商業用途**，使用時請遵守相關法規與隱私政策。
