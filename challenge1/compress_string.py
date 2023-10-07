"""Compress an input string."""
import time

# NOTE: Matplotlib library was not used in
# in actual compress function. It is optional to plot
# time complexity graph for demonstration when 
# plot_graph is set to True.
import matplotlib.pyplot as plt


# Define a function to compress a string
def compress(input_str):
    """Take an input string and compress it.

    Returns original string if length of string
    is not reduced.
    """
    
    # Return an empty string if the input is empty
    if not input_str:
        return ""
    # Return an empty string if the input is None
    if input_str is None:
        return ""
    compressed_str = ""
    count = 1

    # Iterate through the input string
    for i in range(1, len(input_str)):
        # If the current character is the same as the previous one,
        # increment the count.
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            # If a different character is encountered,
            # append the character and its count to the compressed string.
            compressed_str += input_str[i - 1] + str(count)
            count = 1

    # Append the last character and its count to the compressed string
    compressed_str += input_str[-1] + str(count)

    # Check if the compressed string is shorter than the original string
    if len(compressed_str) < len(input_str):
        return compressed_str
    else:
        # If not, return the original string
        return input_str


def calculate_execution_time(input_size):
    # Create an input string of the specified size
    input_str = "a" * input_size
    start_time = time.time()  # Record the start time

    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time

    # print execution time and string
    # print(f"Input: {input_str}; Execution Time: {execution_time}")
    return execution_time


# Check if the script is being run directly
if __name__ == "__main__":
    # toggle plot time complexity graph.
    # If True, graph will be ploted using matplotlib
    plot_graph = False
    
    # Prompt the user to enter a string
    input_str = input("Enter a string: ")

    start_time = time.time()  # Record the start time
    
    # Call the compress function with the user's input
    compressed_result = compress(input_str)
    
    end_time = time.time()  # Record the end time
    
    # Calculate the execution time (time complexity)
    # Convert to milliseconds.
    execution_time = (end_time - start_time) * 1000
    """Time complexity of the function is recorded as
    execution_time. 
    
    The longer the input string, the longer the execution_time.
    A graph of execution time complexity can be plotted.
    To plot graph, set plot_graph to True.
    """

    # Print the compressed string.
    # OR the original string based on the compression criteria.
    print(f"Compressed string: {compressed_result}; Execution Time in MilliSeconds: {execution_time:.4f}")

    if plot_graph:
        # Different input sizes to test
        input_sizes = [10, 100, 1000, 10000, 100000]
        execution_times = []

        for size in input_sizes:
            execution_time = calculate_execution_time(size)
            execution_times.append(execution_time)

        # Plot the data
        # plt.scatter(input_sizes, execution_times, label='Execution Time', s=10)
        plt.plot(input_sizes, execution_times, "o-", label="Execution Time")
        plt.xlabel("Input Size")
        plt.ylabel("Execution Time (seconds)")
        plt.title("Execution Time vs. Input Size")
        plt.grid(True)
        plt.legend()

        # Add Big O notation line for reference (linear time complexity)
        plt.plot(
            input_sizes,
            [size / 50000 for size in input_sizes],
            label="O(n)",
            linestyle="dashed",
        )

        # Annotate data points with labels
        for i, (x, y) in enumerate(zip(input_sizes, execution_times)):
            plt.text(x, y, f"{y:.4f}", fontsize=8, ha="right", va="bottom")

        # Display the plot
        plt.show()
