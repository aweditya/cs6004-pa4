import sys
import json

def read_category_counts(file_path):
    category_sums = {}
    category_counts = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                category = parts[1]
                count = int(parts[2])

                if category in category_sums:
                    category_sums[category] += count
                    category_counts[category] += 1
                else:
                    category_sums[category] = count
                    category_counts[category] = 1

    category_averages = {category: category_sums[category] / category_counts[category] for category in category_sums}

    return category_averages

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    category_averages = read_category_counts(file_path)
    print(json.dumps(category_averages, indent=4))

