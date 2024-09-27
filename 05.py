students = [113, 175, 12]

if __name__ == '__main__':
    for student in students:
        print(f"Full groups: {student//24}. Small group size: {student % 24}.")