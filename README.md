# PubSumImplementationPython

Merhaba!

Bu içerikte PubSub’ın tam olarak ne olduğundan ve GCP üzerinden python aracılığıyla PubSub’ın kullanımını ele almaya çalışacağım.

PubSub Nedir?

Pub-Sub, açılımını tahmin edebileceğiniz üzere publisher ve subscriber kelimelerine tekabül ediyor. Kısaca işlevini, bulut sistemlerinde uygulamaların küçük parçalara ayrılarak daha kolay işlem yapılmasına olanak sağlayan bir mesajlaşma sistemi gibi düşünebiliriz.

Bir mesajlaşma sisteminden beklentilerimiz neler olabilir?

Mesajları kaybetmemek.
Mesajları çoklamamak.
Mesajları belirli bir sırada teslim etmek. (PubSub bunu FIFO(first in first out) yapısıyla gerçekleştirir.)
pubsub-architecture
Pub/Sub client ile server bağımlılığını ortadan kaldıran asenkron bir mesajlama servisidir. Asenkron sistemler, senkron sistemlerin aksine aynı anda birden fazla isteği işleyebilirler. İstek yollanır, bu istek işlenir ve bu işleme esnasında başka bir istek daha yollanırsa o istek de işlenir.   Pub/Sub ile bu iletimi gerçek zamanlı ve yüksek tutarlılıkla gerçekleştirmek hedeflenir.

Biraz terminoloji?

Mesaj, data. Bu data string olabilir, sayı olabilir, yapısal olmayan bir data olabilir. Kısaca mesaj, iletilecek olan datadır.

Publisher, veriyi yollayan her bir servis. Yani aslında veriyi üreten producer gibi düşünebilriiz.

Subsriber, o yayıncıya abone olan yani datayı alan, consume eden tüketen taraf oluyor.

Topic, kısaca mesajların toplandığı ve mesajların sıralı şekilde gönderilmesini sağlayan kategoriler olarak düşünebiliriz.

Devamındaki implementasyonları sizin için hazırlamış olduğum aşağıdaki youtube videosundan takip edebilirsiniz.

[![PubSumImplementationPython](https://img.youtube.com/vi/e1AoKDlxMlg/1.jpg)](https://www.youtube.com/watch?v=e1AoKDlxMlg "PubSumImplementationPython")

