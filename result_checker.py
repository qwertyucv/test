import json

def check_results():
    try:
        with open('result.json') as f:
            data = json.load(f)
        
        assert 'generation_time' in data, "Missing generation_time"
        assert 'sorting_time' in data, "Missing sorting_time"
        assert data['sorting_time'] > 0, "Sorting time must be positive"
        
        print("✅ Results are valid!")
        return True
    except Exception as e:
        print(f"❌ Validation failed: {str(e)}")
        return False

if __name__ == "__main__":
    check_results()
