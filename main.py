from mock_log_service import MockLogService

def main(): 
    mocklog = MockLogService()
    mocklog.simulate(1)
    
    #[print(x) for x in mocklog.logs]

if __name__ == "__main__":
    main()