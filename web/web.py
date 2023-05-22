#网页制作
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        df = pd.read_csv(io.StringIO(f.stream.read().decode("UTF8")), delimiter=',', nrows=20)
        columns = df.columns.tolist()
        values = [df[col].values.tolist() for col in columns]
        return render_template('index.html', columns=columns, values=values)

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    if request.method == 'POST':
        df = pd.read_csv(request.form['file'], delimiter=',')
        plt.plot(df['topic'], df['mark_overall'])
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(host="localhost", port=8088)
    #检索
file="D:\essay\EssayChecker-server\web\database\essaychecker.csv"
csvPD=pd.read_csv(file)

for i in range(len(csvPD)):
    if str(csvPD['topic'][i])=="":
        print(csvPD['topic'][i]
print(data.loc[data['topic'] == '', ['', '']])
data = pd.read_excel(excel_file, index_col='topic')        
print(data.loc['']
      #json格式转换
app = Flask(__name__)

@app.route('/api/result', methods=['GET'])
def get_result():
    result = {}
    return jsonify(result)
