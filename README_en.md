---

# TAVCD (Traffic Accident Verdict Compensation Dataset)

[中文版](https://github.com/Chrouos/TAVCD-Traffic-Accident-Verdict-Compensation-Dataset-/blob/main/README_zh.md)

## **Introduction**
TAVCD (Traffic Accident Verdict Compensation Dataset) is a labeled dataset focusing on **Taiwanese traffic accident verdicts**, covering court decisions, accident details, personal injuries, property damages, and compensation amounts. This dataset is suitable for **academic research, legal analysis, and machine learning model training**, particularly in NLP tasks such as text classification, named entity recognition (NER), and information extraction.

### **Dataset Overview**
- **Dataset Size**: A total of **1000** verdicts
- **Annotation Method**: Independently annotated by two annotators (`Labeler_1` & `Labeler_2`) to ensure accuracy
- **Data Format**: JSONL (`.jsonl`)


### **Data Overview**

```json
{
  "input": "臺灣新北地方法院民事判決107年度重訴字第311號原告李秋義訴訟代理人李嘉民林翰榕律師被告尤于方訴訟代理人趙政揚律師（法律扶助）被告三重汽車客運股份有限公司法定代理人李博仁上列當事人間請求侵權行為損害賠償事件，原告提起刑事附帶民事訴訟，經本院刑事庭裁定移送前來（106年度原交重附民字第3號），本院於民國107年9月26日言詞辯論終結，判決如下：主文被告應連帶給付原告新臺幣壹佰貳拾捌萬肆仟柒佰柒拾元，及被告尤于方自民國一○六年十一月二十七日起、被告三重汽車客運股份有限公司自民國一○六年十一月十五日起，均至清償日止，按週年利率百分之五計算之利息。原告其餘之訴駁回。訴訟費用由被告連帶負擔百分之十二，餘由原告負擔。本判決第一項於原告以新臺幣肆拾貳萬捌仟元為被告供擔保後，得假執行；但被告如以新臺幣壹佰貳拾捌萬肆仟柒佰柒拾元為原告預供擔保，得免為假執行。原告其餘假執行之聲請駁回。事實及理由壹、程序方面一、按因犯罪而受損害之人，於刑事訴訟程序得附帶提起民事訴訟，對於被告及依民法負賠償責任之人，請求回復其損害。前項請求之範圍，依民法之規定。又附帶民事訴訟除本編有特別規定外，準用關於刑事訴訟之規定。但經移送或發回、發交於民事庭後，應適用民事訴訟法。訴狀送達後，原告不得將原訴變更或追加他訴，但擴張或減縮應受判決事項之聲明者，不在此限，刑事訴訟法第487條、第490條、民事訴訟法第255條第1項第3款分別定有明文。經查，原告原以尤于方為被告，就其由本院106年度原交易字第67號刑事業務過失傷害案件審理部分提起刑事附帶民事訴訟，依民法侵權行為之法律關係，聲明請求：1、被告應給付原告新臺幣（下同）1063萬5984元及自起訴狀繕本送達翌日起至清償日止，按週年利率百分之五計算之利息。2、請准供擔保宣告假執行（見附民卷第7至21頁）。嗣起訴狀繕本送達被告後，原告於民國106年11月6日提出民事準備狀主張系爭車禍發生時，被告尤于方為三重汽車客運股份有限公司（下稱三重客運公司）所僱用並執行職務，爰聲請追加三重客運公司為被告，暨變更原訴之聲明第1項主張被告應連帶負給付責任等語（見附民卷第113至118頁）；嗣本院刑事庭准予追加被告並裁定移送前來，原告再於107年7月23日本院言詞辯論期日中陳述變更訴之聲明為：1、被告應連帶給付原告1063萬5984元及自民事準備狀繕本送達翌日起至清償日止，按週年利率百分之五計算之利息。...",
  "output": {
    "事發經過": "被告尤于方係被告三重客運公司所屬265路線公車之司機，為從事駕駛業務之人，其於105年11月18日上午9時51分許，駕駛三重客運公司所有之車牌號碼000-00號營業用大客車（下稱本案公車），沿新北市板橋區忠孝路往四川路方向行駛，迨行至忠孝路與四川路交岔路口欲右轉駛入四川路時，竟疏未注意即貿然右轉，適原告徒步由西向東穿越四川路口之行人穿越道旁時，被告尤于方所駕駛之本案公車右前車頭與原告發生碰撞",
    "事故日期": "105年11月18日",
    "傷勢": "受有左側近端肱骨骨折、左側股骨頸骨折之傷害",
    "職業": "中校退伍",
    "精神賠償": "30萬",
    "醫療費用": "10萬9026",
    "每日居家看護金額": "2200",
    "居家看護天數": "361",
    "居家看護費用": "79萬4200",
    "每日住院看護金額": "2200",
    "住院看護天數": "286",
    "住院看護費用": "62萬9200",
    "看護總額": "62萬9200",
    "每日營業收入": "",
    "營業損失天數": "",
    "營業損失": "",
    "每日工作收入": "",
    "工作損失天數": "",
    "工作損失": "",
    "事故車出廠日期": "",
    "折舊方法": "",
    "耐用年數": "",
    "零件": "",
    "材料": "",
    "工資": "",
    "鈑金": "",
    "塗裝": "",
    "烤漆": "",
    "修車費用": "",
    "交通費用": "6萬6,870",
    "財產損失": "",
    "賠償金額總額": "168萬1320",
    "被告肇責": "80",
    "保險給付金額": ""
  }
}
```

---

## **Directory Structure & Data Content**

### **1. Original Verdict Data**
> Stored in the `Source/Verdict/` directory, containing raw verdict content and processed text.

- **`judgement`**: Full text of the verdict (including line breaks)
- **`cleanJudgement`**: Plain text version with special symbols removed
- **`opinion`**: Extracted judge's ruling from `judgement`
- **`cleanOpinion`**: Plain text version of the judge's ruling (special symbols removed)

### **2. Annotated Data**
> Stored in `Source/Labeler_1/` and `Source/Labeler_2/`, containing manually labeled results.

- **`name`**: Annotated field name (e.g., “Accident Date,” “Total Compensation Amount”)
- **`value`**: Annotated content
- **`the_surrounding_words`**: Contextual information around the annotated content
- **`position`**: Location of the annotated content in the verdict
  - `start_position` & `end_position` (character indices within the text)

### **3. Machine Learning Training Data**
> Data formatted for NLP model training, suitable for information extraction and generative AI applications.

- **`finetuning_training_data_golden.jsonl`**:
  - `input`: Full verdict content
  - `output`: JSON structure containing all annotated fields
- **`finetuning_training_data.jsonl`**:
  - `subject`: Annotated field name
  - `input`: Contextual text around the annotation (split based on punctuation)
  - `output`: Extracted content

---

## **Codebase**

+ `regular_fields.py` - Defines annotation field categories such as **accident details, injuries, compensation amounts,** etc.
+ `processed_to_format.py` - Converts dataset formats for different application scenarios.

---

## **Annotation Fields**
The TAVCD dataset includes the following categories:

### **(1) Accident Information**
- Accident Date
- Accident Description
- Vehicle Manufacturing Date

### **(2) Personal Injury & Compensation**
- Injuries
- Occupation
- Home Nursing Days / Cost / Daily Rate
- Hospital Nursing Days / Cost / Daily Rate
- Medical Expenses
- Emotional Distress Compensation
- Daily Work Income
- Work Loss Days / Compensation Amount

### **(3) Vehicle & Property Damage**
- Depreciation Method
- Durability Years
- Repair Costs (Painting / Labor / Coating / Bodywork / Parts / Materials)
- Property Damage
- Transportation Costs

### **(4) Verdict Compensation & Insurance Payments**
- Defendant Liability Percentage
- Total Compensation Amount
- Insurance Payout Amount

### **(5) Business Losses**
- Daily Business Income
- Business Loss Days / Compensation Amount

### **(6) Other Information**
- Miscellaneous (other damages or special information)
- Remarks

---

## **Usage**
The TAVCD dataset can be used for:
1. **Legal Analysis**: Researching trends in Taiwan’s court rulings on traffic accident compensation.
2. **Machine Learning / NLP Training**: Training models for verdict parsing, information extraction, and classification.
3. **Text Annotation Applications**: Key information tagging, relationship extraction, and event identification.

### **Simple Data Loading Example**
```python
import json

def load_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

# Load data
data = load_jsonl("finetuning_training_data_golden.jsonl")

# Display the first entry
print(json.dumps(data[0], indent=2, ensure_ascii=False))
```

### **Convert Data Format**
```bash
python ./processed_to_format.py \
    --type format_data_text \
    --data_path finetuning_training_data_golden.jsonl \
    --output_path ./instruction/
```

---

## **Contributions & Contact**
If you have suggestions or find any issues with this dataset, please contact us via:
- Submit a [GitHub Issue](https://github.com/Chrouos/TAVCD-Traffic-Accident-Verdict-Compensation-Dataset-/issues)
- Directly contact the dataset maintainers

---

## **License**
This dataset is available **for academic research and non-commercial use only**. Please comply with relevant regulations and privacy policies when using it.