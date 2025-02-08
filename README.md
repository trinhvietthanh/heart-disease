<img src="/SCREEN-SHOTS/Heart-Disease-Prediction-System-banner.png" />

## Abstract 
<p> 
  Ngày nay, bệnh tim là bệnh phổ biến nhất. Tuy nhiên, điều trị bệnh tim khá tốn kém và không phải ai cũng có thể chi trả được. Do đó, chúng ta có thể giảm bớt vấn đề này một phần bằng cách dự đoán bệnh tim trước khi nó trở nên nguy hiểm thông qua Hệ thống Dự đoán Bệnh Tim sử dụng Học Máy và Khai thác Dữ liệu. Nếu chúng ta có thể phát hiện vấn đề bệnh tim ở giai đoạn đầu, điều đó sẽ rất hữu ích cho việc điều trị. Các kỹ thuật Học Máy và Khai thác Dữ liệu được sử dụng để xây dựng Hệ thống Dự đoán Bệnh Tim. Trong lĩnh vực y tế sinh học, có sự sử dụng rộng rãi dữ liệu y tế dưới dạng văn bản, hình ảnh, v.v., nhưng dữ liệu đó hiếm khi được xem xét và khai thác. Vì vậy, chúng ta có thể tránh được vấn đề này bằng cách giới thiệu Hệ thống Dự đoán Bệnh Tim. Hệ thống này sẽ giúp giảm chi phí và nâng cao chất lượng điều trị cho bệnh nhân tim. Hệ thống có thể xác định các vấn đề phức tạp và đưa ra các quyết định y tế thông minh. Hệ thống có thể dự đoán khả năng bệnh nhân mắc các vấn đề về tim dựa trên các chỉ số như huyết áp, tuổi, giới tính, cholesterol và đường huyết. Đồng thời, hiệu suất của hệ thống sẽ được so sánh qua việc tính toán ma trận nhầm lẫn. Điều này sẽ giúp tính toán độ chính xác, độ chuẩn và độ hồi tưởng. Tổng thể, hệ thống cung cấp hiệu suất cao và độ chính xác tốt hơn.
</p>

## Introduction
<p>
Ngành công nghiệp chăm sóc sức khỏe thu thập một lượng lớn dữ liệu chứa thông tin tiềm ẩn, có ích cho việc đưa ra các quyết định hiệu quả. Để cung cấp kết quả chính xác và đưa ra các quyết định hiệu quả trên dữ liệu, một số kỹ thuật khai thác dữ liệu tiên tiến được sử dụng. Trong nghiên cứu này, một Hệ thống Dự đoán Bệnh Tim (HDPS) được phát triển sử dụng các thuật toán Naive Bayes và Decision Tree để dự đoán mức độ rủi ro của bệnh tim. Hệ thống sử dụng 13 tham số y tế như tuổi, giới tính, huyết áp, cholesterol và béo phì để thực hiện dự đoán. HDPS dự đoán khả năng bệnh nhân mắc bệnh tim. Nó cho phép rút ra kiến thức quan trọng, ví dụ như các mối quan hệ giữa các yếu tố y tế liên quan đến bệnh tim và các mô hình, để được thiết lập. Chúng tôi đã sử dụng mạng nơ-ron đa lớp với thuật toán lan truyền ngược (back propagation) làm thuật toán huấn luyện. Kết quả thu được đã chỉ ra rằng hệ thống chẩn đoán được thiết kế có thể dự đoán hiệu quả mức độ rủi ro của bệnh tim.
</p>

### Aim
<p> 
Để dự đoán bệnh tim dựa trên các giá trị tham số đầu vào do người dùng cung cấp và dữ liệu được lưu trữ trong cơ sở dữ liệu, hệ thống có thể thực hiện các bước sau:

- Thu thập dữ liệu đầu vào: Người dùng nhập các giá trị của các tham số y tế như tuổi, giới tính, huyết áp, cholesterol, đường huyết, v.v.

- Tiền xử lý dữ liệu: Hệ thống xử lý và làm sạch dữ liệu từ cơ sở dữ liệu và các giá trị đầu vào của người dùng để chuẩn hóa hoặc chuyển đổi chúng thành định dạng phù hợp với mô hình dự đoán.

- Sử dụng thuật toán học máy: Các thuật toán như Naive Bayes, Decision Tree hoặc Mạng Nơ-ron (Neural Networks) sẽ được áp dụng để phân tích và dự đoán mức độ rủi ro của bệnh tim dựa trên dữ liệu đầu vào và mô hình học đã được huấn luyện.

- Dự đoán kết quả: Hệ thống đưa ra dự đoán về khả năng người dùng mắc bệnh tim, dựa trên các thông số y tế đã nhập và dữ liệu trong cơ sở dữ liệu.

- Cung cấp kết quả và giải thích: Hệ thống cung cấp kết quả dự đoán, có thể kèm theo giải thích về mức độ rủi ro của người dùng, và thông tin về các yếu tố y tế ảnh hưởng đến tình trạng sức khỏe của họ.
</p>

### Objective
<p>
  Mục tiêu chính của dự án này là phát triển một hệ thống dự đoán bệnh tim. Hệ thống này có thể khám phá và trích xuất các kiến thức tiềm ẩn liên quan đến bệnh tật từ bộ dữ liệu lịch sử về bệnh tim. Hệ thống dự đoán bệnh tim nhằm khai thác các kỹ thuật khai thác dữ liệu trên bộ dữ liệu y tế để hỗ trợ trong việc dự đoán các bệnh tim.

Bằng cách sử dụng các phương pháp khai thác dữ liệu, hệ thống sẽ phân tích các thông tin lịch sử về bệnh tim, tìm ra các mối quan hệ và mô hình giữa các yếu tố y tế, từ đó đưa ra những dự đoán chính xác hơn về nguy cơ mắc bệnh tim của bệnh nhân. Hệ thống này không chỉ giúp cải thiện chất lượng điều trị mà còn giảm chi phí chăm sóc sức khỏe bằng cách dự đoán sớm các nguy cơ tiềm ẩn.
</p>

### Project Scope
<p>
 Dự án này có phạm vi rộng, vì nó không chỉ dành cho một tổ chức cụ thể. Dự án này sẽ phát triển phần mềm tổng quát, có thể được áp dụng bởi bất kỳ tổ chức, doanh nghiệp nào. Hơn nữa, phần mềm này sẽ cung cấp các tính năng tiện ích cho người dùng của nó. Đồng thời, phần mềm cũng sẽ cung cấp một lượng lớn dữ liệu tổng hợp, giúp người dùng có cái nhìn tổng quát về các thông tin và kết quả phân tích, từ đó hỗ trợ trong việc đưa ra quyết định kinh doanh và chăm sóc sức khỏe.

Điều này giúp mở rộng khả năng áp dụng của phần mềm, không chỉ trong lĩnh vực y tế mà còn có thể được sử dụng trong các ngành khác liên quan đến việc phân tích dữ liệu và dự đoán.
</p>

## System Analysis
### Modules:
- **Patient Login:-** *Bệnh nhân đăng nhập vào hệ thống bằng ID và mật khẩu của mình.*
- **Patient Registration:_** *Nếu bệnh nhân là người dùng mới, họ sẽ nhập thông tin cá nhân và tạo ID cùng mật khẩu để có thể đăng nhập vào hệ thốn.*
- **My Details:-** *Bệnh nhân có thể xem các thông tin cá nhân của mình.*
- **Disease Prediction:-** *Bệnh nhân sẽ nhập các giá trị tham số đầu vào. Hệ thống sẽ nhận giá trị đầu vào và dự đoán bệnh dựa trên các giá trị dữ liệu đầu vào mà bệnh nhân đã chỉ định, đồng thời hệ thống cũng sẽ gợi ý các bác sĩ dựa trên khu vực địa lý của bệnh nhân*
- **Search Doctor:-** *Bệnh nhân có thể tìm bác sĩ bằng cách chỉ định tên, địa chỉ hoặc loại bác sĩ.*
- **Feedback:-** *Bệnh nhân sẽ đưa ra phản hồi và phản hồi này sẽ được báo cáo cho quản trị viên.*
- **Doctor Login:-** *Bác sĩ sẽ truy cập vào hệ thống bằng ID người dùng và mật khẩu của mình.*
- **Patient Details:-** *Bác sĩ có thể xem thông tin cá nhân của bệnh nhân.*
- **Notification:-** *Quản trị viên và bác sĩ sẽ nhận được thông báo về số lượng người đã truy cập hệ thống và những bệnh nào đã được dự đoán bởi hệ thống.*
- **Admin Login:-** *Quản trị viên có thể đăng nhập vào hệ thống bằng ID và mật khẩu của mình.*
- **Add Doctor:-** *Quản trị viên có thể thêm thông tin bác sĩ mới vào cơ sở dữ liệu.*
- **Add Dataset:-** *Quản trị viên có thể thêm tệp dữ liệu vào cơ sở dữ liệu.*
- **View Doctor:-** *Quản trị viên có thể xem các bác sĩ cùng với thông tin cá nhân của họ.*
- **View Disease:-** *Quản trị viên có thể xem các thông tin về các bệnh đã được lưu trữ trong cơ sở dữ liệu.*
- **View Patient:-** *Quản trị viên có thể xem các thông tin bệnh nhân đã truy cập hệ thống.*
- **View Feedback:-** *Quản trị viên có thể xem các phản hồi đã được cung cấp bởi người dùng.*
  
### Technology Used:
- #### Languages:
  - ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
  - ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
  - ![JAVASCRIPT](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
  - ![PYTHON](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
- #### FrameWork:
  - ![BOOTSTRAP](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
  - ![DJANGO](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
- #### Machine-Learning Algorithms:
  - <a href="https://en.wikipedia.org/wiki/Gradient_boosting">**GRADIENT BOOSTING ALGORITHM**</a>
  - <a href="https://en.wikipedia.org/wiki/Logistic_regression">**LOGISTIC REGRESSION**</a>
- #### ML/DL:
  - ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
  - ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
  - ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
- Database:
  - ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
- ### Explain Result:
  - Lime (https://github.com/marcotcr/lime)
- #### Data-Set for training:
  - <a href="https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data">Click here for DATA-SET</a>
- #### IDE:
  - ![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
  - ![pyCharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
- #### OS used for testing:
  - ![MacOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)
  - ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
  - ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

## Demo Video
- Click to view
<a href="https://youtu.be/8tRgrn5xDdU" target="_blank"><img src="/SCREEN-SHOTS/check.png" width="450" alt="KDD promo video"/></a>

## Run Locally
Install dependencies

```bash
  pip3 install -r requirement.txt
```

Start the server

```bash
  python manage.py runserver
```  

## Model Training(Machine Learning)

```javascript
def prdict_heart_disease(list_data):
    csv_file = Admin_Helath_CSV.objects.get(id=1)
    df = pd.read_csv(csv_file.csv_file)

    X = df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)
    nn_model = GradientBoostingClassifier(n_estimators=100,learning_rate=1.0,max_depth=1, random_state=0)
    nn_model.fit(X_train, y_train)
    pred = nn_model.predict([list_data])
    print("Neural Network Accuracy: {:.2f}%".format(nn_model.score(X_test, y_test) * 100))
    print("Prdicted Value is : ", format(pred))
    dataframe = str(df.head())
    return (nn_model.score(X_test, y_test) * 100),(pred)
```



## Output Screen-shots
Khi ứng dụng được chạy, một trang Chào mừng sẽ xuất hiện.
<img src="/SCREEN-SHOTS/check.png" />

Admin Dash-board:
<img src="/SCREEN-SHOTS/AdminDashboard.png" />

Nhập thông tin về bệnh tim để kiểm tra sức khỏe của bản thân:
<img src="/SCREEN-SHOTS/AddHeartDetail.png" />

Vì những thông tin này được lưu trữ trong cơ sở dữ liệu, chúng ta cũng có thể truy xuất các kết quả trong quá khứ:
<img src="/SCREEN-SHOTS/SearchLogs1.png" />

Xem chi tiết tài khoản:
<img src="/SCREEN-SHOTS/chos.png" />

Đăng ký tài khoản bác sĩ:
<img src="/SCREEN-SHOTS/Doctors.png" />

Đăng ký tài khoản bệnh nhân:
<img src="/SCREEN-SHOTS/Patient.png" />

Lựa chọn tài khoản:
<img src="/SCREEN-SHOTS/user_choose.png">

Chính sách:
<img src="/SCREEN-SHOTS/policy.png">

