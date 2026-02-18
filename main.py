from mockLogService import MockLogService

def main(): 
    mocklog = MockLogService()
    mocklog.simulate(300)
    
    [print(x) for x in mocklog.logs]

if __name__ == "__main__":
    main()