from product_data import products

# TODO: Step 1 - Print out the products to see the data that you are working with.
print("First 5 available products:")
print(products[:5])

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    preference = input("Input a preference: ")
    if preference.strip():  # ignore empty
        customer_preferences.append(preference.lower())  # lowercase for consistency
    response = input("Do you want to add another preference? (Y/N): ").upper()

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)
print("Customer preferences (set):", customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }
    converted_products.append(converted_product)  # <-- FIXED

# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))  

# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    for product in products:
        match_count = count_matches(product["tags"], customer_tags)
        if match_count > 0:
            recommendations.append({
                "name": product["name"],
                "match_count": match_count
            })

    # sort by matches (highest first)
    recommendations.sort(key=lambda x: x["match_count"], reverse=True)
    return recommendations  # <-- FIXED

# TODO: Step 7 - Call your function and print the results
print("\nRecommended Products:")
results = recommend_products(converted_products, customer_preferences)
for result in results:
    print(f"{result['name']} - Matches: {result['match_count']}")
    
# DESIGN MEMO (write below in a comment): 
#1. What core operations did you use (e.g., intersections, loops)? Why? 
#I used loops to help sort through products faster and through the use of tags the products were found faster. I also used sets to help get rid of duplications through products.
#2. How might this code change if you had 1000+ products?
#The code would change to a database structure instead of a list to help quicken up the process of searching through everything.
