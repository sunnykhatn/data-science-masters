def product_of_numbers(lst):
  """Calculates the product of all numbers in a nested list.

  Args:
    lst: A nested list containing numbers.

  Returns:
    The product of all numbers in the list.
  """

  flat_list = []
  def flatten(lst):
    for item in lst:
      if isinstance(item, (int, float)):
        flat_list.append(item)
      elif isinstance(item, (list, tuple, set)):
        flatten(item)
      elif isinstance(item, dict):
        for key, value in item.items():
          if isinstance(key, (int, float)):
            flat_list.append(key)
          # Check if value is iterable before recursion
          if isinstance(value, (list, tuple, set, dict)):
            flatten(value)

  flatten(lst)

  product = 1
  for num in flat_list:
    product *= num
  return product

# Example usage:
list1 = [1, 2, 3, 4, [44, 55, 66, True], False, (34, 56, 78, 89, 34), {1, 2, 3, 3, 2, 1}, {1: 34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)}, [56, 'data science'], 'Machine Learning']

result = product_of_numbers(list1)
print(result)