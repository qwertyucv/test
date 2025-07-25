import json
import glob
import os

def generate_leaderboard():
    results = []
    for file in glob.glob("results/*/*.json"):
        try:
            with open(file) as f:
                content = f.read().strip()
                if not content:
                    continue
                    
                data = json.loads(content)
                username = os.path.basename(os.path.dirname(file))
                total_time = data["generation_time"] + data["sorting_time"]
                results.append({
                    "user": username,
                    "generation": data["generation_time"],
                    "sorting": data["sorting_time"],
                    "total": total_time
                })
                print(f"Found result for {username}: {total_time:.2f} ms")
        except Exception as e:
            print(f"Error processing {file}: {str(e)}")
            continue
    
    if not results:
        print("No results found!")
        return "# 🏆 Leaderboard\n\nNo results yet!"
    
    results.sort(key=lambda x: x["total"])
    
    md = "# 🏆 Leaderboard\n\n"
    md += "| Position | User | Generation (ms) | Sorting (ms) | Total (ms) |\n"
    md += "|----------|------|-----------------|--------------|------------|\n"
    
    for i, res in enumerate(results[:10]):
        md += f"| {i+1} | {res['user']} | {res['generation']:.2f} | {res['sorting']:.2f} | **{res['total']:.2f}** |\n"
    
    print(f"Generated leaderboard with {len(results)} results")
    return md

if __name__ == "__main__":
    leaderboard = generate_leaderboard()
    with open("LEADERBOARD.md", "w") as f:
        f.write(leaderboard)
