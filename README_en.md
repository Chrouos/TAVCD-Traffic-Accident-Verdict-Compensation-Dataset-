---

# TAVCD (Traffic Accident Verdict Compensation Dataset)

[中文版](https://github.com/Chrouos/TAVCD-Traffic-Accident-Verdict-Compensation-Dataset-/blob/main/README_zh.md)

## **Introduction**
TAVCD (Traffic Accident Verdict Compensation Dataset) is a labeled dataset focusing on **Taiwanese traffic accident verdicts**, covering court decisions, accident details, personal injuries, property damages, and compensation amounts. This dataset is suitable for **academic research, legal analysis, and machine learning model training**, particularly in NLP tasks such as text classification, named entity recognition (NER), and information extraction.

### **Dataset Overview**
- **Dataset Size**: A total of **1000** verdicts
- **Annotation Method**: Independently annotated by two annotators (`Labeler_1` & `Labeler_2`) to ensure accuracy
- **Data Format**: JSONL (`.jsonl`)

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