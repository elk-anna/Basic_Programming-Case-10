def format_address(street, city, province, postal_code):
    formatted_address = f"Street: {street}, City: {city}, {province} ({postal_code})"
    return formatted_address

print(format_address("Jl. Merdeka No. 10", "Bandung", "Jawa Barat", "40123"))
