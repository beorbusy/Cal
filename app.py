import flet as ft

def main(page: ft.Page):
    page.title = "Simple Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Input Fields
    num1_field = ft.TextField(label="First Number", keyboard_type=ft.KeyboardType.NUMBER)
    num2_field = ft.TextField(label="Second Number", keyboard_type=ft.KeyboardType.NUMBER)

    # Result Display
    result_text = ft.Text(value="Result will appear here", color="blue", size=20)

    # Function to Perform Addition
    def calculate(e):
        try:
            num1 = float(num1_field.value)
            num2 = float(num2_field.value)
            result = num1 + num2
            result_text.value = f"The sum of {num1} and {num2} is {result}"
            result_text.color = "green"
        except ValueError:
            result_text.value = "Please enter valid numbers!"
            result_text.color = "red"
        page.update()

    # Calculate Button
    calculate_button = ft.ElevatedButton("Calculate", on_click=calculate)

    # Adding Components to Page
    page.add(
        num1_field,
        num2_field,
        calculate_button,
        result_text,
    )

# Run the app
ft.app(target=main)
