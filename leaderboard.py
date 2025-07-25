import json
import glob

def generate_leaderboard():
    results = []
    for file in glob.glob("results/*/*.json"):
        try:
            with open(file) as f:
                data = json.load(f)
                username = file.split('/')[1]
                results.append({
                    "user": username,
                    "generation": data["generation_time"],
                    "sorting": data["sorting_time"],
                    "total": data["generation_time"] + data["sorting_time"]
                })
        except:
            continue
    
    results.sort(key=lambda x: x["total"])
    
    md = "# 🏆 Leaderboard\n\n"
    md += "| Position | User | Generation (ms) | Sorting (ms) | Total (ms) |\n"
    md += "|----------|------|-----------------|--------------|------------|\n"
    
    for i, res in enumerate(results[:10]):
        md += f"| {i+1} | {res['user']} | {res['generation']:.2f} | {res['sorting']:.2f} | **{res['total']:.2f}** |\n"
    
    if not results:
        md += "| No results yet! | | | | |\n"
    
    return md

if __name__ == "__main__":
    leaderboard = generate_leaderboard()
    with open("LEADERBOARD.md", "w") as f:
        f.write(leaderboard)
