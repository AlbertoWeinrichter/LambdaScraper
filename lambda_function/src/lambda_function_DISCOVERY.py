from webdriver_wrapper import WebDriverWrapper


def lambda_handler(event, context):
    driver = WebDriverWrapper()

    driver.get_url('https://www.brainyquote.com/topics/{topic}-quotes'.format(topic=event["topic"]))

    nodes = driver.find_elements_by_xpath('//*[@title="view quote"]')

    return [n.get_attribute("href") for n in nodes]
