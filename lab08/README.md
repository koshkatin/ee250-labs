# Partners: Faith Klein, Tina Habibi

# Question 1: What are the denominations of the US coins from the green, blue and orange distributions? Can you think why the coins from the same denomination might show variation in weight although they are specified to be of the same weight? If your vending machine had a weight sensor, how would you use the weight of a coin that was just inserted to find the denomination?

    The denominations of the US coins from the green, blue, and orange distributions are a cent, nickel, and dollar, respectively. Coins from the same denomination might show variation in weight although they are specified to be of the same weight due to manufacturing error, any additional substances that are stuck on the coin, and natural wear and tear of the coins over time. If the vending machine has a weight sensor, it could use the weight of the inserted coin to find the denomination by using classification to match the given weight into a proper weight category based on known weight ranges of different denominations. 

# Question 2. We can shine light on the coin and measure the reflected amount of light which should be proportional (directly or in some non-linear way) to the size/area of the coin. Can you guess which sensor on the Grove Pi Kit can be used for this purpose?

    The sensor would be a light sensor which detects the intensity of light, so it can be used in order to measure the reflected amount of light. 

# Question 3: Which of the following datasets are linearly separable? Justify your answer.

    It seems like datasets A, C, and D are linearly separable because these are the 3 datasets where we can draw a line and all the orange dots fall on one side of it while all the blue dots fall on the other side. 

# Question 4. Sometimes we need more than a simple hyperplane to separate the datasets of the two classes. What are some other simple geometric entities other than a simple plane/line that can be used to separate some of the data points that were not linearly separable?

    Some other geometric entities that can be used to separate some of the data points that were not linearly separable are a circle, heart, triangle, two lines, and parabola. The circle, heart, and triangle all work similarly, where we can have multiple classes being inside the shape versus outside the shape. Entities like a parabola or two lines can have classes that fall within a certain side of the function, like below or above. The euqatuions represent circle, pair of lines, parabola, ellipse, and hyperbola.


# Question 5. For the example shown in the figure, what is approximately the output of the neuron? the bias is -2[if anybody has any confusion]

    w0 = -2
    XtransposeW = (2x1) + (1x-2) + (2x3) = 6 

    Y = g(w0 + XtransposeW)
    Y = g(-2+6) 
    Y = g(4)

    g(z) = σ(z) = 1 / (1 + e^(-z))
    g(4) = 1/(1+e^-4) = 0.982
