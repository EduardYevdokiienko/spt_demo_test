def test_e2e(page, main_page, search_page, streamer_page):
    main_page.open()
    main_page.expect_page_is_opened()
    main_page.click_search_icon()
    search_page.expect_page_is_opened()
    search_page.input_value_and_search_("StarCraft II")
    search_page.scroll_down_times_(2)
    search_page.choose_streamer_(3)
    streamer_page.take_screenshot_of_streamer("new_screenshot")
