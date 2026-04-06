# 🤖 Generative AI with Large Language Models
## 📘 Week 02 — Fine-Tuning, Evaluation & Efficient Adaptation

This module focuses on improving LLM performance using:

- Fine-tuning techniques
- Instruction tuning
- Evaluation metrics
- Benchmarking
- Parameter Efficient Fine-Tuning (PEFT)

---

# 1️⃣ Fine-Tuning LLMs with Instructions

## 🔹 Why Fine-Tuning?

Prompting (zero-shot, one-shot, few-shot) has limitations:

### ❌ Drawbacks
- Inconsistent outputs
- Large prompts required
- Expensive (token cost)
- Limited control over behavior

👉 Solution: Fine-tuning

---

## 🔹 What is Fine-Tuning?

Fine-tuning is training a pre-trained LLM on task-specific data to improve performance.

---

## 🔹 Instruction Tuning

Training model using instructions like:

```
Input: Translate English to French
Output: Bonjour
```

Helps model follow instructions better.

---

## 🔹 Prompt Template Libraries

Reusable structured prompts for consistent input.

Example:
```
"Translate the following text: {input_text}"
```

---

# 2️⃣ Fine-Tuning Process

## 🔹 Step 1: Prepare Instruction Dataset

Dataset format:

- Input (instruction)
- Output (expected response)

---

## 🔹 Step 2: Training Splits

Split data into:

- Training Set → Used for learning  
- Validation Set → Used for tuning  
- Test Set → Used for final evaluation  

---

## 🔹 Step 3: Training

Model learns by minimizing **loss function**.

Loss = difference between predicted and actual output.

---

# 3️⃣ Fine-Tuning on Single Task

## 🔹 Problem: Catastrophic Forgetting

When model forgets previous knowledge after fine-tuning on a new task.

---

## 🔹 How to Avoid Catastrophic Forgetting

### ✅ Strategies

1. Identify important knowledge  
2. Fine-tune on multiple tasks  
3. Use parameter-efficient fine-tuning (PEFT)  

---

# 4️⃣ Multi-Task Fine-Tuning

Train model on multiple tasks simultaneously.

### 🔹 Benefits

- Better generalization  
- Reduced overfitting  
- Less forgetting  

---

# 5️⃣ Model Evaluation Metrics

## 🔹 Accuracy

```
Accuracy = Correct Predictions / Total Predictions
```

Used for classification tasks.

---

## 🔹 ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

Used for:
- Summarization
- Text generation

---

### 🔹 ROUGE-1 (Unigram)

Measures overlap of single words.

#### Recall:
```
Recall = Overlap / Reference
```

#### Precision:
```
Precision = Overlap / Generated
```

#### F1 Score:
```
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

---

### 🔹 ROUGE-2 (Bigram)

Measures overlap of word pairs.

---

### 🔹 ROUGE-L

Measures longest common subsequence.

---

## 🔹 Disadvantages of ROUGE

❌ Focuses on exact word match  
❌ Ignores meaning/context  
❌ Not good for creative tasks  

---

## 🔹 BLEU Score (Bilingual Evaluation Understudy)

Used for:
- Machine translation

---

### 🔹 Key Concepts

- Unigram → Single words  
- Bigram → Two-word sequences  
- N-gram → Sequence of N words  

---

## 🔹 BLEU Characteristics

- Measures precision  
- Penalizes short outputs  
- Uses n-gram overlap  

---

# 6️⃣ Benchmarks for LLM Evaluation

## 🔹 GLUE

- General language understanding tasks

---

## 🔹 SuperGLUE

- More challenging version of GLUE

---

## 🔹 HELM

- Holistic evaluation across multiple scenarios

---

## 🔹 MMLU

- Multi-task language understanding

---

## 🔹 BIG-bench

- Large benchmark for diverse tasks

---

# 7️⃣ Parameter Efficient Fine-Tuning (PEFT)

## 🔹 What is PEFT?

Fine-tuning only a small subset of model parameters.

---

## 🔹 Benefits

✅ Can run on single GPU  
✅ Faster training  
✅ Lower memory usage  
✅ Less catastrophic forgetting  

---

# 8️⃣ Types of PEFT

## 🔹 1. Selective Fine-Tuning

Only some layers are trained.

---

## 🔹 2. Reparameterization

### 🔸 LoRA (Low-Rank Adaptation)

- Adds small matrices to model
- Does not change original weights

---

## 🔹 3. Additive Methods

### 🔸 Adapters

- Small layers added to model
- Train only adapter layers

---

### 🔸 Soft Prompting

- Learn prompt embeddings instead of weights

---

# 9️⃣ LoRA (Low-Rank Adaptation)

## 🔹 Key Idea

Instead of updating full model:

👉 Add small trainable matrices

---

## 🔹 Benefits

- Efficient
- Low memory usage
- Faster training

---

# 🔟 Soft Prompting

## 🔹 What is Soft Prompt?

Learnable embeddings added to input prompt.

---

## 🔹 Advantage

- No need to modify model weights
- Efficient for multiple tasks

---

# 📌 Module Summary

In this module, you learned:

- Fine-tuning vs prompting
- Instruction tuning
- Training process and datasets
- Catastrophic forgetting
- Multi-task learning
- Evaluation metrics (Accuracy, ROUGE, BLEU)
- Benchmark datasets
- Parameter Efficient Fine-Tuning (PEFT)
- LoRA and Soft Prompting

---

# 🎯 Interview Questions & Answers

## ❓ What is fine-tuning?

Training a pre-trained model on task-specific data to improve performance.

---

## ❓ Why not rely only on prompting?

Because prompting:
- Is inconsistent
- Expensive
- Limited in control

---

## ❓ What is catastrophic forgetting?

When a model forgets previous knowledge after learning a new task.

---

## ❓ How to avoid catastrophic forgetting?

- Multi-task training  
- PEFT techniques  
- Balanced datasets  

---

## ❓ What is instruction tuning?

Training models using structured input-output instructions.

---

## ❓ What is PEFT?

Fine-tuning only a small part of the model to save resources.

---

## ❓ What is LoRA?

A PEFT technique that adds low-rank matrices instead of modifying full model weights.

---

## ❓ What is soft prompting?

Learning embeddings for prompts instead of updating model weights.

---

## ❓ Difference between ROUGE and BLEU?

- ROUGE → Recall-based (summarization)  
- BLEU → Precision-based (translation)  

---

## ❓ What is ROUGE-1 vs ROUGE-2?

- ROUGE-1 → Unigram overlap  
- ROUGE-2 → Bigram overlap  

---

## ❓ What is accuracy?

Correct predictions divided by total predictions.

---

## ❓ What are LLM benchmarks?

Standard datasets used to evaluate model performance.

Examples:
- GLUE
- SuperGLUE
- MMLU

---

# 🚀 Final Takeaway

This module takes you from:

👉 Using LLMs  
to  
👉 Improving and evaluating LLMs

Now you understand:

- How to fine-tune models
- How to measure performance
- How to optimize training efficiently

This is core knowledge for:

- AI engineers
- LLM engineers
- Agentic AI developers
- ML researchers

## 👨‍💻 Author

Arslan  
Learning Python → Web → Databases → AI → Agentic Systems 🚀