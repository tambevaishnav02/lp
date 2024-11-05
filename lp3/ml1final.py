def f(x):
    # Function we want to minimize
    return (x + 3) ** 2
def f_derivative(x):
    # Derivative of the function, which represents the gradient
    return 2 * (x + 3)
def gradient_descent(starting_x, learning_rate, tolerance, max_iters):
    x = starting_x
    for i in range(max_iters):
        # Calculate gradient at current point
        grad = f_derivative(x)
        # Update x in the opposite direction of the gradient
        new_x = x - learning_rate * grad
        # Check for convergence
        if abs(new_x - x) < tolerance:
            
            print(f"Converged at iteration {i+1}")
            break
        x = new_x
    return x
# Parameters
starting_x = 2         # Initial value of x
learning_rate = 0.1    # Step size
tolerance = 1e-6       # Tolerance for convergence
max_iters = 1000       # Maximum number of iterations
# Run Gradient Descent
local_minimum = gradient_descent(starting_x, learning_rate, tolerance, max_iters)
print("Local minimum at x =", local_minimum)
