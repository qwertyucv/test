import json
import os

def check_results():
    try:
        if not os.path.exists("result.json"):
            print("❌ File result.json not found!")
            return False
            
        with open('result.json') as f:
            content = f.read().strip()
            if not content:
                print("❌ File result.json is empty!")
                return False
            if "generation_time" not in content or "sorting_time" not in content:
                print(f"❌ Invalid JSON format: {content}")
                return False
                
            data = json.loads(content)
            
            assert 'generation_time' in data, "Missing generation_time"
            assert 'sorting_time' in data, "Missing sorting_time"
            assert isinstance(data['generation_time'], (int, float)), "Invalid generation_time type"
            assert isinstance(data['sorting_time'], (int, float)), "Invalid sorting_time type"
            assert data['sorting_time'] > 0, "Sorting time must be positive"
            
            print("✅ Results are valid!")
            print(f"Generation time: {data['generation_time']} ms")
            print(f"Sorting time: {data['sorting_time']} ms")
            return True
            
    except Exception as e:
        print(f"❌ Validation failed: {str(e)}")
        return False

if __name__ == "__main__":
    check_results()
