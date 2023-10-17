#!/bin/bash

# Function to add two numbers
add_numbers() {
  local num1=$1
  local num2=$2
  local result=$((num1 + num2))
  echo $result
}

# Call the function and store the result
addition=$(add_numbers $INPUT_VAR1 $INPUT_VAR2)

# Display the result
echo "The sum of ${INPUT_VAR1} and ${INPUT_VAR2} is: $addition"

if [ -n "$addition" ]; then
  echo "set GITHUB_OUTPUT variable..."
  echo "sum=$addition" >> "$GITHUB_OUTPUT"
  echo "set GITHUB_ENV variable..."
  echo "add=$addition" >> "$GITHUB_ENV"
else
  echo "sum=None_or_empty" >> "$GITHUB_OUTPUT"
  echo "add=None_or_empty" >> "$GITHUB_ENV"
fi
