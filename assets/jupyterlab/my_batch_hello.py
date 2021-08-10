
def my_batch_main(*wml_args):
    import os,logging
    from datetime import datetime
    
    print(datetime.now().strftime("%H:%M:%S"),"my_batch_main started")

    in_data = wml_args['scoring']['input_data_references']
    # out_data = wml_args['scoring']['output_data_reference']
    # input and output data references not used in this example
    #logging.info("input/output data ignored")
        
    print(wml_args)

    print(datetime.now().strftime("%H:%M:%S"),"my_batch_main done")
