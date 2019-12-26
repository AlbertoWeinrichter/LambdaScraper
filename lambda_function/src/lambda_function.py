from webdriver_wrapper import WebDriverWrapper


def lambda_handler(event, context):
    driver = WebDriverWrapper()
    driver.get_url('{url}'.format(url=event["url"]))

    content = driver.get_inner_html("//*[contains(@class, 'quoteContent')]/div/p[1]")
    author = driver.get_inner_html("//*[contains(@class, 'quoteContent')]/div/p/a")

    return {
        "content": content,
        "author": author
    }
