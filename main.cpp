#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <fstream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main() {
    const size_t N = 50000;
    std::vector<double> numbers(N);
    
    auto start_gen = std::chrono::high_resolution_clock::now();
    for (size_t i = 0; i < N; ++i) {
        numbers[i] = N - i;
    }
    auto end_gen = std::chrono::high_resolution_clock::now();
    
    auto start_sort = std::chrono::high_resolution_clock::now();
    std::sort(numbers.begin(), numbers.end());
    auto end_sort = std::chrono::high_resolution_clock::now();
    
    json result;
    result["generation_time"] = std::chrono::duration<double, std::milli>(end_gen - start_gen).count();
    result["sorting_time"] = std::chrono::duration<double, std::milli>(end_sort - start_sort).count();
    
    std::ofstream("result.json") << result.dump(4);
    return 0;
}
