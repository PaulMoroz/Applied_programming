       
  <div id="readme" class="Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0">
    <article class="markdown-body entry-content container-lg" itemprop="text"><h1><a id="user-content-проектування-rest-api" class="anchor" aria-hidden="true" href="#проектування-rest-api"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Проектування REST API</h1>
<p>Проектуючи REST API визначають:</p>
<ul>
<li>сутності, що містяться в системі</li>
<li>операції, які можна виконувати над тими чи іншими сутностями</li>
<li>які HTTP методи використовуються до яких операцій</li>
<li>структура запитів та відповідей для тих чи інших операцій</li>
<li>які HTTP статус коди повертаються в тій чи іншій ситуації</li>
<li>як відбувається авторизація</li>
</ul>
<p>Всі ці рішення документуються, щоб всі члени команди розуміли всі деталі API, яке потрібно реалізувати. Також така документація може використовуватись користувачами API щоб розуміти які операції можна виконувати, які дані передавати в запитах, які дані очікувати у відповідь і т.д.</p>
<p>В процесі реалізації спроектованого REST API, особливо при засосуванні методології розробки Agile, деякі його деталі можуть змінюватись, тоді документація змінюється відповідно.</p>
<p>REST API можна описувати різними способами, однак найпопулярнішим є стандарт <a href="https://swagger.io/specification/" rel="nofollow">OpenAPI</a> (колишня Swagger Specification). OpenAPI специфікації описуються в форматі YAML або JSON.</p>
<p>В даній лабораторній роботі потрібно визначити як буде виглядати API системи згідно з варіантом та описати його в форматі OpenAPI версії 3.</p>
<h2><a id="user-content-варіанти" class="anchor" aria-hidden="true" href="#варіанти"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Варіанти</h2>
<p>Варіант 1. Створити сервіс переказу коштів між користувачами, кожен користувач має власний гаманець та можливість переказувати чи отримувати кошти від іншого користувача.
Варіант 2. Створити сервіс коротких (404 символи) заміток (із тегами) для кожного користувача із можливістю перегляду, редагування і видалення, а також надавати доступ редагувати замітку іншими користувачами (до 5 користувачів). Також надати можливість бачити статистику користувача, скільки повідомлень, коли редаговані і ким.
Варіант 3. Створити сервіс оголошень + CRUD із двома рівнями повідомлень. Оголошення повинні бути локальними та публічними. Локальні оголошення тільки для користувачів, що знаходяться в тому ж місці. Публічні для всіх, навіть для не користувачів сервісу.
Варіант 4. Створити сервіс кредитування користувачів на основі даних, що користувач вводить при реєстрації, кошти для кредитування видаються із бюджету 517 000 грн ставка 30%. Також реалізувати можливість погашення кредиту.
Варіант 5. Написати сервіс статей (2000 символів). Статті є публічними для всіх, зареєстровані користувачі можуть редагувати статтю та очікувати на схвалення її модераторами (користувачі із більшими правами). Передбачити варіант редагування, коли стаття на розгляді модератором, а інший користувач її теж редагує. Модератори мають бачити статті, які очікують їх схвалення.
Варіант 6. Написати сервіс простий інтернет магазин. Користувачі можуть купувати один із 8 товарів, які є в обмеженій кількості на складі, не допустити можливості продажу одного і того ж товару кільком користувачам.
Варіант 7. Створити сервіс для резервування аудиторій на певну дату час та проміжок часу від 1 години до 5 днів. Користувачі мають можливість резервувати аудиторії, а також редагувати, скасовувати та видаляти їх. Застерегти користувачів від накладок (два користувачі не можуть зарезервувати аудиторію на певний період час)
Варіант 8. Написати сервіс для купівлі та бронювання квитків на концерти, події і т.д. Користувачі мають можливість купувати квиток, бронювати квиток, скасовувати бронь. Унеможливити купівлю чи бронювання одного і того ж квитка кількома користувачами.
Варіант 9. Написати сервіс для створення плейлистів. Користувач може мати як приватні (видимі тільки для нього), так і публічні (видимі для всіх) плейлисти. Публічні плейлисти можуть редагувати всі користувачі.
Варіант 10. Створити сервіс для календаря подій. Користувач має можливість створювати подію, редагувати її, видаляти, долучати інших користувачів до події, переглядати перелік всіх створених події, та подій до яких він долучений.
Варіант 11. Створити сервіс для проведення онлайн занять. Повинні бути користувачі двох рівнів – викладачі та учні. Викладачі можуть створювати, видаляти, редагувати курс, переглядати перелік створених курсів, долучати студентів до курсу. До курсу може бути долучено не більше 5 студентів. Студенти можуть переглядати всі дані лише тих курсів, до яких вони долучені. Також студенти можуть надсилати на участь у якомусь курсі, а викладач має можливість прийняти або відхилити запит.
Варіант 12. Створити сервіс для збереження та редагування рейтингу студентів. Для зберігання даних про студента використовувати json. Також реалізувати можливість отримання списку кращих за рейтингом студентів.
Варіант 13. Написати сервіс для роботи з сімейним бюджетом на спільному рахунку. В сім’ї повинно бути не менше 3 людей. Кожен користувач має можливість переглядати бюджет, додавати в нього кошти, знімати кошти на свій персональний рахунок. Також передбачити можливість збереження та виведення переліку витрат та доходів як сім’ї загалом, так і кожного її учасника.
Варіант 14. Створити сервіс для прокату авто. Користувачі сервісу можуть бути двох рівнів – адміністратори та пасажири. Адміністратори можуть додавати та видаляти авто із системи, редагувати інформацію про авто. Пасажири можуть переглядати каталог та бронювати авто на певний час.
Варіант 15. Написати сервіс для роботи аптеки. Провізор може додавати препарати в базу, видаляти, редагувати інформацію про них. Користувач може переглядати інформацію про препарати, здійснювати купівлю, якщо немає препарату в наявності, то його можна додати в попит.
Варіант 16. Написати сервіс для роботи кінотеатру. Адміністратор може складати розклад показу фільмів, з урахуванням тривалості фільму та зайнятості залу, редагувати розклад, видаляти та додавати фільми.
Варіант 17. Свій варіант (після узгодження з викладачем)</p>
<h2><a id="user-content-рекомендації" class="anchor" aria-hidden="true" href="#рекомендації"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Рекомендації</h2>
<ul>
<li>OpenAPI специфікації досить великі за ромізром, тому для спрощення процесу створення нової API можна розпочати з прикладу специфікації "Swagger Petstore" з <a href="https://editor.swagger.io" rel="nofollow">Swagger Editor</a>. Даний приклад використовує специфікацію OpenAPI 2, його можна конвертувати в OpenAPI 3 засобами Swagger Editor (Editor / Convert to OpenAPI 3). Після конвертації в OpenAPI 3 даний приклад можна використати для створення власної специфікації, при цьму варто старатись обмежитись мінімально необхідною специфікацією, без копіювання непотрібних елементів з прикладу.</li>
</ul>
<h2><a id="user-content-хід-роботи" class="anchor" aria-hidden="true" href="#хід-роботи"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Хід роботи</h2>
<ol>
<li>Визначити набір сутностей, що будуть в системі та описати які зв'язки будуть між ними та які операції над ними можна виконувати</li>
<li>Створити файл <code>swagger.yaml</code> з описом API у форматі OpenAPI 3</li>
<li>Перевірити валідність створеного <code>swagger.yaml</code> за допомогою <a href="https://editor.swagger.io" rel="nofollow">Swagger Editor</a>.</li>
</ol>
<h2><a id="user-content-критерії-оцінювання" class="anchor" aria-hidden="true" href="#критерії-оцінювання"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Критерії оцінювання</h2>
<ol>
<li>Студент має описати словами створену специфікацію REST API</li>
<li>Файл <code>swagger.yaml</code> має містити валідний опис API в форматі OpenAPI 3
<blockquote>
<p>Перевірити валідність можна за допомогою <a href="https://editor.swagger.io" rel="nofollow">Swagger Editor</a></p>
</blockquote>
</li>
<li>Використані коректні HTTP методи та HTTP статус коди для тих чи інших операцій
<blockquote>
<p>Перевірити у візуалізації специфікації Swagger Editor</p>
</blockquote>
</li>
<li>Окрім опису відповіді при успішному виконання також мають описуватись відповіді при тих чи інших помилках
<blockquote>
<p>Перевірити опис відповідей при HTTP статус кодах відмінних від 200</p>
</blockquote>
</li>
</ol>
<h2><a id="user-content-виконання-лабораторної-роботи" class="anchor" aria-hidden="true" href="#виконання-лабораторної-роботи"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Виконання лабораторної роботи</h2>
<p>Варіант 1. Створити сервіс переказу коштів між користувачами, кожен користувач має власний гаманець та можливість переказувати чи отримувати кошти від іншого користувача.</p>
<h3><a id="user-content-визначити-набір-сутностей" class="anchor" aria-hidden="true" href="#визначити-набір-сутностей"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Визначити набір сутностей</h3>
<p>В даній системі будуть наступні сутності:</p>
<ul>
<li>Користувач</li>
<li>Гаманець</li>
<li>Транзакція</li>
</ul>
<p>Користувач може мати кілька гаманців. Після авторизації користувачем ми можемо виконувати тільки операції над гаманцями користувача від імені якого ми авторизувались. Користувач може ініціювати транзакцію переказу грошей зі свого гаманця на будь-який інший. Тільки власник гаманця має доступ до транзакцій, що асоційовані з відповідним гаманцем.</p>
<h3><a id="user-content-створити-файл-swaggeryaml" class="anchor" aria-hidden="true" href="#створити-файл-swaggeryaml"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Створити файл <code>swagger.yaml</code></h3>
<p><a href="/ihor-pyvovarnyk/university-python/blob/master/Labs/L2/swagger.yaml">swagger.yaml</a></p>
</article>
  </div>

    </div>

  


  <details class="details-reset details-overlay details-overlay-dark" id="jumpto-line-details-dialog">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get">
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>

    <div class="Popover anim-scale-in js-tagsearch-popover"
     hidden
     data-tagsearch-url="/ihor-pyvovarnyk/university-python/find-definition"
     data-tagsearch-ref="master"
     data-tagsearch-path="Labs/L2/README.md"
     data-tagsearch-lang="Markdown"
     data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_symbol&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_symbol&quot;,&quot;repository_id&quot;:209779082,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Markdown&quot;,&quot;originating_url&quot;:&quot;https://github.com/ihor-pyvovarnyk/university-python/blob/master/Labs/L2/README.md&quot;,&quot;user_id&quot;:null}}"
     data-hydro-click-hmac="c8acdc1287f1888a1cf194e758601bc6824a93f8ca6756598e7ed5cce33be5aa">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box box-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>




  </div>
</div>

    </main>
  </div>

  </div>

          
<div class="footer container-xl width-full p-responsive" role="contentinfo">
    <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between flex-sm-items-center pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
      <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mr-lg-4" href="https://github.com">
        <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>
      <ul class="list-style-none d-flex flex-wrap col-12 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0">&copy; 2020 GitHub, Inc.</li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
            <li class="js-cookie-consent-preferences-link-container mr-3 mr-lg-0" hidden="hidden">
  <button data-ga-click="Footer, go to cookie preferences, text:cookie preferences" class="btn-link js-cookie-consent-preferences-link" type="button">Cookie Preferences</button>
</li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to help, text:help" href="https://docs.github.com">Help</a></li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://services.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
      </ul>
    </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
    </button>
    You can’t perform that action at this time.
  </div>


  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path></svg>
    <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

    <div class="js-cookie-consent-banner" hidden>
  <div class="hx_cookie-banner p-2 p-sm-3 p-md-4">
    <div style="max-width: 1194px;" class="Box hx_cookie-banner-box box-shadow-medium mx-auto">
    <div class="Box-body border-0 py-0 px-3 px-md-4">
      <div class="js-main-cookie-banner hx_cookie-banner-main">
          <div class="d-md-flex flex-items-center py-3">
            <p class="f5 flex-1 mb-3 mb-md-0">
              
  We use <span class="text-bold">optional</span> third-party analytics cookies to understand how you use GitHub.com so we can build better products.

              <span class="btn-link js-cookie-consent-learn-more">Learn more</span>.
            </p>
            <div class="d-flex d-md-block flex-wrap flex-sm-nowrap">
              <button class="btn btn-outline flex-1 mr-1 mx-sm-1 m-md-0 ml-md-2 js-cookie-consent-accept">Accept</button>
              <button class="btn btn-outline flex-1 ml-1 m-md-0 ml-md-2 js-cookie-consent-reject">Reject</button>
            </div>
          </div>
        </div>

        <div class="js-cookie-details hx_cookie-banner-details" hidden>
          <div class="d-md-flex flex-items-center py-3">
            <p class="f5 flex-1 mb-2 mb-md-0">
              
  We use <span class="text-bold">optional</span> third-party analytics cookies to understand how you use GitHub.com so we can build better products.

              <br>
              You can always update your selection by clicking <span class="text-bold">Cookie Preferences</span> at the bottom of the page.
              For more information, see our <a href="https://docs.github.com/en/free-pro-team@latest/github/site-policy/github-privacy-statement">Privacy Statement</a>.
            </p>
          </div>

          <div class="d-md-flex flex-items-center py-3 border-top">
            <div class="f5 flex-1 mb-2 mb-md-0">
              <h5 class="mb-1">Essential cookies</h5>
              <p class="f6 mb-md-0">We use essential cookies to perform essential website functions, e.g. they're used to log you in. 
                <a href="https://docs.github.com/en/github/site-policy/github-subprocessors-and-cookies">Learn more</a>
              </p>
            </div>
            <div class="text-right">
              <h5 class="text-blue">Always active</h5>
            </div>
          </div>

          <div class="d-md-flex flex-items-center py-3 border-top">
            <div class="f5 flex-1 mb-2 mb-md-0">
              <h5 class="mb-1">Analytics cookies</h5>
              <p class="f6 mb-md-0">We use analytics cookies to understand how you use our websites so we can make them better, e.g. they're used to gather information about the pages you visit and how many clicks you need to accomplish a task. 
                <a href="https://docs.github.com/en/github/site-policy/github-subprocessors-and-cookies">Learn more</a>
              </p>
            </div>
            <div class="text-right">
              <div class="BtnGroup mt-1 mt-md-0 ml-2">
                <button class="btn btn-outline BtnGroup-item js-accept-analytics-cookies" type="button">Accept</button>
                <button class="btn btn-outline BtnGroup-item js-reject-analytics-cookies" type="button">Reject</button>
              </div>
            </div>
          </div>

          <div class="text-right py-3 border-top">
            <button class="btn btn-primary js-save-cookie-preferences" type="button" disabled>Save preferences</button>
          </div>
        </div>
</div></div>  </div>
</div>


  </body>
</html>

