# Here is an example of how to use the problem statements, requirements, and interface.
from tqdm import tqdm
from datasets import Dataset, load_dataset

TEMPLATE = f"""{row['FINAL_PROBLEM_STATEMENT']}

Requirements:
{row['FINAL_REQUIREMENT']}

New interfaces introduced:
{row['FINAL_INTERFACE']}
"""

if __name__ == "__main__":
    swebench_pro = load_dataset('ScaleAI/SWE-bench_Pro', split='test')

    for row in tqdm(swebench_pro):
        problem_statement = TEMPLATE.format(row=row)
        print(problem_statement)